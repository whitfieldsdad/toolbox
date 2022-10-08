import fnmatch

import glob

import datetime

from typing import Optional, List, Iterable, Set, Any, Union

import json
import dateutil.parser

import psutil

STRS = Iterable[str]


def main(process_ids: Optional[STRS] = None, process_names: Optional[STRS] = None):
    for p in iter_processes(process_ids=process_ids, process_names=process_names):
        txt = json.dumps(p, indent=4, sort_keys=True)
        print(txt)


def iter_processes(process_ids: Optional[STRS] = None, process_names: Optional[STRS] = None) -> dict:
    process_ids = frozenset(process_ids) if process_ids else None
    process_names = frozenset(process_names) if process_names else None

    processes = list(psutil.process_iter())
    for process in processes:
        if process_ids and process.pid not in process_ids:
            continue

        if process_names and not matches(process.name(), process_names):
            continue

        yield process.as_dict()


def str_to_strs(data: Optional[str]) -> List[str]:
    if not data:
        return []
    return data.split(',')


def extract_ints(values: Iterable[Any]) -> Set[int]:
    results = set()
    for value in values:
        if isinstance(value, int):
            results.add(value)
        elif isinstance(value, str):
            try:
                results.add(int(value))
            except ValueError:
                continue
    return results


def to_datetime(t: Union[str, int, float, datetime.date, datetime.datetime, None]) -> Optional[datetime.datetime]:
    if t is not None:
        t = _to_datetime(t)
        if t:
            return t.astimezone()


def _to_datetime(t: Union[str, int, float, datetime.date, datetime.datetime, None]) -> Optional[datetime.datetime]:
    if t is not None:
        if isinstance(t, datetime.datetime):
            return t
        elif isinstance(t, str):
            return dateutil.parser.parse(t)
        elif isinstance(t, (int, float)):
            return datetime.datetime.fromtimestamp(t)
        elif isinstance(t, datetime.datetime):
            return t
        elif isinstance(t, datetime.date):
            return datetime.datetime.combine(t, datetime.datetime.min.time())
        else:
            raise TypeError("Unsupported timestamp format: %s", type(t).__name__)


def matches(values: Union[str, Iterable[str]], patterns: Union[str, Iterable[str]] = None):
    values = _to_lowercase_strings(values)
    patterns = _to_lowercase_strings(patterns)

    for value in values:
        for pattern in patterns:
            if value == pattern or (glob.has_magic(pattern) and fnmatch.fnmatch(value, pattern)):
                return True
    return False


def _to_lowercase_strings(values: Union[str, Iterable[str]]):
    values = [values] if isinstance(values, str) else list(values)
    values = list(map(str.lower, values))
    return values


if __name__ == "__main__":
    def cli():
        import argparse

        parser = argparse.ArgumentParser('Learn more about processes')
        parser.add_argument('--process-ids', '-p', help='List of PIDs (e.g. 8659,8688-8691)')
        parser.add_argument('--process-names', '-n', help='List of process names (e.g. "ir_agent,*exe')
        kwargs = vars(parser.parse_args())

        main(**kwargs)

    cli()
