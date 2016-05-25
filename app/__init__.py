# from sqlalchemy import create_engine
# from pytz import timezone
# import tzlocal
from config import configure_app
from flask import Flask, render_template
from models import Luggage, db, Archive
from routes import luggage
import flask.ext.whooshalchemy as whooshalchemy
from flask_moment import Moment
import pytz
from flask_sslify import SSLify
import helpers

flask_app = Flask(__name__, template_folder='templates')

SSLify(flask_app)

configure_app(flask_app)
db.init_app(flask_app)
moment = Moment(flask_app)

flask_app.register_blueprint(luggage)

whooshalchemy.whoosh_index(flask_app, Luggage)

@flask_app.teardown_appcontext
def close_db(error=None):
    """Closes the database again at the end of the request."""
    # Flask does .remove() automatically at the end of each HTTP request ("view" functions),
    # so the session is released by the current thread.
    pass

# TODO: move filters and helpers to their own file
def datetimefilter(value, format="%I:%M %p"):
    tz = pytz.timezone('US/Eastern') # timezone you want to convert to from UTC
    utc = pytz.timezone('UTC')
    value = utc.localize(value, is_dst=None).astimezone(pytz.utc)
    local_dt = value.astimezone(tz)
    return local_dt.strftime(format)

@flask_app.context_processor
def utility_processor():
    return dict(current_year=helpers.currentyear, locations=helpers.locations, is_production=helpers.is_production)

flask_app.jinja_env.filters['datetimefilter'] = datetimefilter
