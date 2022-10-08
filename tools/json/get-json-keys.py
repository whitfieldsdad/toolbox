from json import JSONEncoder as _JSONEncoder

import argparse
import itertools
import json
from typing import Any


class JSONEncoder(_JSONEncoder):
    def default(self, obj) -> Any:
        if isinstance(obj, set):
            return sorted(obj)
        else:
            return super().default(obj)


def main(input_path: str):
    data = read_json_file(input_path)
    if isinstance(data, list) and all(isinstance(v, dict) for v in data):
        keys = set(itertools.chain.from_iterable(row.keys() for row in data))
    elif isinstance(data, dict):
        keys = set(data.keys())
    else:
        raise ValueError("Unsupported input data format")

    txt = json.dumps(keys, cls=JSONEncoder)
    print(txt)


def read_json_file(path: str) -> Any:
    with open(path) as file:
        return json.load(file)


if __name__ == "__main__":
    def cli():
        arg_parser = argparse.ArgumentParser()
        arg_parser.add_argument("-i", "--input-path", required=True)

        args = vars(arg_parser.parse_args())
        main(**args)

    cli()
