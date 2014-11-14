######################################################################
# Cloud Routes Web Application
# -------------------------------------------------------------------
# HTTP Request Reaction - Forms Class
######################################################################

from wtforms import TextField, SelectField
from wtforms.validators import DataRequired, URL
from ..base import BaseReactForm


class ReactForm(BaseReactForm):
    ''' Class that creates a HTTP Request Reaction form for the dashboard '''
    url = TextField(
        "url",
        validators=[URL(message='URL required and must be in a valid format')])
    request_type = SelectField(
        "Request Type",
        choices=[('get', 'GET Request'), ('post', 'POST Request')],
        validators=[DataRequired(message='You must select an HTTP(S) request type')])
    post_body = TextField("POST Body")
    request_headers = TextField("Request Headers")

if __name__ == '__main__':
    pass
