import csv
from collections import namedtuple


def read_file(file_name):
    """
    Read csv file, skip the header row
    """
    with open(file_name) as f:
        reader = csv.reader(f, delimiter=',', quotechar='"')
        # Skip the header
        next(reader)
        yield from reader


LANGUAGE_NT = namedtuple('Language', 'english vietnamese remarks')
