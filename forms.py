from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, BooleanField
from wtforms.validators import URL, InputRequired, NumberRange, Optional, Length

class AddPetForm(FlaskForm):
    """Form for adding new pets"""
    name = StringField("Pet Name", validators=[InputRequired(message='Missing pet name')])
    species = StringField("Species", validators=[InputRequired(message='Enter a valid species.')])
    photo_url = StringField("Photo URL", validators=[Optional(), URL(require_tld=True)])
    age = IntegerField("Age", validators=[NumberRange(min=0), InputRequired()])
    notes = TextAreaField("Notes", validators=[Optional()])

class EditPetForm(FlaskForm):
    """Form to edit existing pet"""
    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    notes = TextAreaField("Comments", validators=[Optional(), Length(min=5)])
    available = BooleanField("Available?")