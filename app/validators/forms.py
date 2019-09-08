from wtforms import Form, StringField, IntegerField
from wtforms.validators import DataRequired, length

from app.libs.enum import ClientTypeEnum


class ClientForm(Form):
    account = StringField(validators=[DataRequired(),
                                      length(min=5, max=32)])
    secret = StringField()
    type = IntegerField(validators=[DataRequired()])

    def validate_type(self, value):
        try:
            client = ClientTypeEnum(value.data)
        except ValueError as e:
            raise e
