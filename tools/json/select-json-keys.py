import argparse
import json
from typing import Tuple, Iterable, Any, Optional, List

JSON_INDENT = 4
SORT_KEYS = True


def main(input_path: str, output_path: Optional[str], keys: Iterable[str]):
    data = read_json_file(input_path)

    if keys:
        data = select_dict_keys(data, keys=keys)

    if output_path:
        write_json_file(path=output_path, data=data)
    else:
        print(json.dumps(data, sort_keys=SORT_KEYS, indent=JSON_INDENT))


def read_json_file(path: str) -> Any:
    with open(path) as file:
        return json.load(file)


def write_json_file(path: str, data: dict) -> Any:
    with open(path, 'w') as fp:
        return json.dump(data, fp=fp, sort_keys=SORT_KEYS, indent=JSON_INDENT)


def select_dict_keys(data: dict, keys: Iterable[str]):
    return dict([(k, v) for (k, v) in data.items() if k in keys])


def str_to_strs(data: Optional[str]) -> List[str]:
    if not data:
        return []
    return data.split(',')


if __name__ == "__main__":
    def cli():
        arg_parser = argparse.ArgumentParser()
        arg_parser.add_argument("-i", "--input-path", required=True)
        arg_parser.add_argument('-o', '--output-path', required=False)
        arg_parser.add_argument("-k", "--keys", default="", required=False)

        args = vars(arg_parser.parse_args())
        args['keys'] = str_to_strs(args['keys'])
        main(**args)

    cli()
