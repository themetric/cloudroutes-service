######################################################################
## Cloud Routes Web Application
## -------------------------------------------------------------------
## Reaction - Forms Class
######################################################################

from wtforms import Form
from wtforms import TextField, PasswordField, SelectField, SelectMultipleField, HiddenField
from wtforms.validators import DataRequired, ValidationError, Email, Length, Required, URL
from wtforms.validators import IPAddress, NumberRange, EqualTo
from ..base import BaseReactForm

class ReactForm(BaseReactForm):
  ''' Class that creates a Reaction form for the dashboard '''

  apikey = TextField("API Key", validators=[DataRequired(message='API Key is a required field')])
  dropletid = TextField("Droplet ID#", validators=[DataRequired(message='Droplet ID# is a required field'), NumberRange(min=1, max=None, message="Droplet ID should be a numeric ID number")])
  call_on = SelectField("Call On", choices=[('failed', 'Failed Monitors'), ('healthy', 'Healthy Monitors')], validators=[DataRequired(message='Call On is a required field')])


if __name__ == '__main__':
  pass