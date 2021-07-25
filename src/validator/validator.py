from marshmallow import Schema
from marshmallow import fields
from marshmallow import post_load
from marshmallow import validate


from src.models.language import Language


class Validator(Schema):
    vietnamese = fields.Str(validate=validate.Length(min=1), required=True)
    english = fields.Str(validate=validate.Length(min=1), required=True)

    class Meta:
        strict = True

    @post_load
    def _make_language(self, data, **kwargs):
        return Language(**data)
