import json
import logging
import argparse
import sys
from typing import Any

import yaml
from yaml import FullLoader

JSON_INDENT = 4
SORT_KEYS = True

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def main(input_path: str, output_path: str):
    data = read_yaml_file(input_path)
    if output_path:
        write_json_file(path=output_path, data=data)
    else:
        print_json(data)


def read_yaml_file(path: str) -> Any:
    with open(path) as file:
        return yaml.load(file, Loader=FullLoader)


def print_json(data: Any):
    print(json.dumps(data))


def write_json_file(data: Any, path: str) -> Any:
    with open(path, 'w') as file:
        json.dump(data, fp=file, indent=JSON_INDENT, sort_keys=SORT_KEYS)


if __name__ == "__main__":
    def cli():
        arg_parser = argparse.ArgumentParser()
        arg_parser.add_argument("-i", "--input-path", required=True)
        arg_parser.add_argument('-o', '--output-path', required=False)

        args = vars(arg_parser.parse_args())
        try:
            main(**args)
        except Exception as e:
            logger.error("Failed to convert JSON file into YAML file: %s", e)
            sys.exit(1)

    cli()
