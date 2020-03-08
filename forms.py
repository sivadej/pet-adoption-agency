from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField
from wtforms.validators import URL, InputRequired, NumberRange, Optional

class AddPetForm(FlaskForm):
    """Form for adding new pets"""
    name = StringField("Pet Name", validators=[InputRequired(message='Missing pet name')])
    species = StringField("Species", validators=[InputRequired(message='Enter a valid species.')])
    photo_url = StringField("Photo URL", validators=[Optional(), URL(require_tld=True)])
    age = IntegerField("Age", validators=[NumberRange(min=0), InputRequired()])
    notes = TextAreaField("Notes", validators=[Optional()])