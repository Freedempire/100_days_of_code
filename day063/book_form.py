from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, ValidationError, NumberRange


# def int_number(min=0, max=0):
#     message = f'The number should be between {min} and {max}.'

#     def _int_number(form, field):
#         if not field.data or int(field.data) > max or int(field.data) < min:
#             raise ValidationError(message)
        
#     return _int_number


class BookForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    author = StringField('Author', validators=[DataRequired()])
    rating = IntegerField('Rating', validators=[DataRequired(), NumberRange(min=0, max=10)])
    submit = SubmitField('Add')