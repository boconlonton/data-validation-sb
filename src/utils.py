import csv
from collections import namedtuple
from contextlib import contextmanager


def read_file(file_name):
    """
    Read csv file, skip the header row
    """
    with open(file_name) as f:
        reader = csv.reader(f, delimiter=',', quotechar='"')
        # Skip the header
        next(reader)
        yield from reader


@contextmanager
def open_file(f_name):
    print(f'opening {f_name}')
    f = open(f_name, 'a')
    try:
        yield f
    finally:
        print(f'closing {f_name}')
        f.close()


LANGUAGE_NT = namedtuple('Language', 'english vietnamese remarks')
