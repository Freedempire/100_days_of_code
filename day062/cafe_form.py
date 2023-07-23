# import re

from flask_wtf import FlaskForm
from wtforms import StringField, URLField, TimeField, SelectField, SubmitField
from wtforms.validators import DataRequired, URL, ValidationError


# def validate_time(form, field):
#     time_pattern = r'^([0-1]\d|2[0-4]):[0-5]\d$'
#     print(re.match(time_pattern, field.data))
#     if re.match(time_pattern, field.data) is None:
#         message = 'Time must be in 24h format, i.e. hh:mm.'
#         raise ValidationError(message)


class CafeForm(FlaskForm):
    name = StringField('Cafe name', validators=[DataRequired()])
    location = URLField('Cafe Location on Google Maps (URL)', validators=[DataRequired(), URL()])
    opening_time = TimeField('Opening Time (24hr format, e.g. 08:00)', validators=[DataRequired()])
    closing_time = TimeField('Closing Time (24hr format, e.g. 17:00)', validators=[DataRequired()])
    coffee_rating = SelectField(
        'Coffee Rating',
        validators=[DataRequired()],
        choices=[
            (5, '☕☕☕☕☕'),
            (4, '☕☕☕☕'),
            (3, '☕☕☕'),
            (2, '☕☕'),
            (1, '☕')
        ]
    )
    wifi_strength_rating = SelectField(
        'Wifi Strength Rating',
        validators=[DataRequired()],
        choices=[
            (5, '💪💪💪💪💪'),
            (4, '💪💪💪💪'),
            (3, '💪💪💪'),
            (2, '💪💪'),
            (1, '💪'),
            (0, '❌')
        ]
    )
    power_socket_availability = SelectField(
        'Power Socket Availability',
        validators=[DataRequired()],
        choices=[
            (5, '🔌🔌🔌🔌🔌'),
            (4, '🔌🔌🔌🔌'),
            (3, '🔌🔌🔌'),
            (2, '🔌🔌'),
            (1, '🔌'),
            (0, '❌')
        ]
    )
    submit = SubmitField('Submit')
