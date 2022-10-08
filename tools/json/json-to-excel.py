import logging
import argparse
import json
import sys
from typing import Any, Optional

import pandas as pd
from pandas import ExcelWriter, DataFrame
from xlsxwriter.worksheet import Worksheet

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

DEFAULT_XLSX_SHEET_NAME = 'Sheet1'

#: Length of the longest field plus 15%.
XLSX_COLUMN_WIDTH_BUFFER = 0.15

JSON_INDENT = 4
SORT_KEYS = True


def main(input_path: str, output_path: str):
    data = read_json_file(input_path)
    write_to_xlsx_file(path=output_path, data=data)


def read_json_file(path: str) -> Any:
    with open(path) as file:
        return json.load(file)


def write_to_xlsx_file(path: str, data: Any):
    with pd.ExcelWriter(path, engine='xlsxwriter') as writer:

        #: If the input is a set of key/value pairs.
        if isinstance(data, dict):
            if all(isinstance(k, str) and isinstance(v, dict) for (k, v) in data.items()):
                for sheet_name in data:
                    df = pd.DataFrame.from_records([data[sheet_name]])
                    create_sheet(writer, df=df, sheet_name=sheet_name)
            else:
                df = pd.DataFrame.from_records([data])
                create_sheet(writer, df=df, sheet_name=DEFAULT_XLSX_SHEET_NAME)

        #: If the input is a list of dictionaries.
        elif isinstance(data, list) and all(isinstance(v, dict) for v in data):
            df = pd.DataFrame.from_records(data)
            create_sheet(writer, df=df)
        else:
            raise ValueError("Unsupported input file structure")


def create_sheet(
        writer: ExcelWriter,
        df: DataFrame,
        sheet_name: Optional[str] = DEFAULT_XLSX_SHEET_NAME) -> Worksheet:

    sheet_name = sheet_name or DEFAULT_XLSX_SHEET_NAME
    df.to_excel(writer, sheet_name=sheet_name, index=False)

    #: Encapsulate the data within a table so the data is sortable within Excel.
    sheet = writer.sheets[sheet_name]
    (max_row, max_col) = df.shape
    sheet.add_table(0, 0, max_row, max_col - 1, {'columns': [{'header': column} for column in df.columns]})

    #: Auto-adjust column widths.
    for i, col in enumerate(df):
        series = df[col]
        max_len = max((series.astype(str).map(len).max(), len(str(series.name)))) + 1
        sheet.set_column(i, i, max_len * (1 + XLSX_COLUMN_WIDTH_BUFFER))
    return sheet


def is_non_nested_dict(data: Any) -> bool:
    return isinstance(data, dict) and not any(isinstance(v, dict) for v in data.values())


if __name__ == "__main__":
    def cli():
        arg_parser = argparse.ArgumentParser()
        arg_parser.add_argument("-i", "--input-path", required=True)
        arg_parser.add_argument('-o', '--output-path', required=True)

        args = vars(arg_parser.parse_args())
        try:
            main(**args)
        except Exception as e:
            logger.error("Failed to convert JSON file into XLSX file: %s", e)
            sys.exit(1)

    cli()
