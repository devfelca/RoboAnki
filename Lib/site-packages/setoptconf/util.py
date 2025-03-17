import csv
from io import StringIO


__all__ = ("csv_to_list")


def csv_to_list(value):
    if isinstance(value, str) and value:
        reader = csv.reader(StringIO(value))
        parsed = next(reader)
        return parsed
    return []
