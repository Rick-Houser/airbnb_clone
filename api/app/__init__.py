from flask import Flask
import os
from flask_json import FlaskJSON
from flask_cors import CORS, cross_origin

app = Flask(__name__)
json = FlaskJSON(app)

env = os.environ.get('AIRBNB_ENV')

# Limited access in production only from production server
if env == "production":
    cors = CORS(app, resources={r"/*": {"origins": ["https://127.0.0.1/",
                                                    "https://158.69.80.142/"]}})
else:
    # access from everywhere in development
    cors = CORS(app, resources={r"/*": {"origins": "*"}})
from views import *
