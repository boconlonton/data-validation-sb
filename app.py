import os
import itertools
import logging
import json
import argparse
import sys
from contextlib import ExitStack

from marshmallow import ValidationError

from src.validator import Validator
from src.utils import read_file
from src.utils import open_file
from src.utils import LANGUAGE_NT


logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
parser = argparse.ArgumentParser()
parser.add_argument('data_path',
                    metavar='data_path',
                    type=str)
args = parser.parse_args()

data_path = args.data_path

validator = Validator()

current_dir = os.path.abspath(os.getcwd())
language_file = os.path.join(current_dir, data_path)
en_file = 'output/en.json'
vi_file = 'output/vi.json'


dict_en = dict()
dict_vi = dict()


for line in read_file(language_file):
    temp = validator.dump(LANGUAGE_NT(*line))
    try:
        obj = validator.load(temp)
        dict_en.update({obj.key: obj.eng})
        dict_vi.update({obj.key: obj.vn})
    except ValidationError as e:
        logger.warning(e.messages)


with ExitStack() as stack:
    f_en = stack.enter_context(open_file(en_file))
    f_vi = stack.enter_context(open_file(vi_file))
    json.dump(dict_vi, f_vi, ensure_ascii=False, indent=4)
    json.dump(dict_en, f_en, ensure_ascii=False, indent=4)
