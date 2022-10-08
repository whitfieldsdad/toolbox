import logging
import argparse
import json
import sys
from typing import Any

import yaml

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def main(input_path: str, output_path: str):
    data = read_json_file(input_path)
    if output_path:
        write_yaml_file(path=output_path, data=data)
    else:
        print_yaml(data)


def read_json_file(path: str) -> Any:
    with open(path) as file:
        return json.load(file)


def write_yaml_file(data: Any, path: str) -> Any:
    with open(path, 'w') as file:
        yaml.dump(data, file)


def print_yaml(data: Any):
    print(yaml.dump(data))


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
