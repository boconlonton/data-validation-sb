import os
import itertools

from marshmallow import ValidationError

from src.validator import Validator
from src.utils import read_file
from src.utils import LANGUAGE_NT

current_dir = os.path.abspath(os.getcwd())
language_file = os.path.join(current_dir, 'data/raw.csv')


validator = Validator()


for line in itertools.islice(read_file(language_file), 50):
    temp = validator.dump(LANGUAGE_NT(*line))
    try:
        obj = validator.load(temp)
        print(obj)
    except ValidationError:
        print('error')
    finally:
        continue
