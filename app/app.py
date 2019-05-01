from flask import Flask
from werkzeug.contrib.fixers import ProxyFix

from blue_api import api

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)

api.init_app(app)

app.run(debug=True)