from flask import Flask

CONFIG = "config"
app = Flask(__name__)

app.config.from_object("config")
