from flask import Flask

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('app.config')

from app import views, models
