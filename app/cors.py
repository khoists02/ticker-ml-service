import os

from flask_cors import CORS

from main import app

origins = ["https://api.mlservice.local"]

cors = CORS(app, resources={r"/api/*": {"origins": origins}})
