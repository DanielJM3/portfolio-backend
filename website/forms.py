from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length, EqualTo
from flask_wtf.file import FileField, FileAllowed, FileRequired

class SampleForm(FlaskForm):
    string = StringField('sample')
    file = FileField('sample', validators=[FileAllowed(['jpg', 'png'])])
    text_area = TextAreaField('sample', validators=[DataRequired()])
    category = SelectField('sample', choices=[('sample_entry', 'Entry Name')])
    boolean = BooleanField('sample')
    submit = SubmitField('Post')
