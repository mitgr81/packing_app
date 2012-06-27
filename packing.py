from flask import Flask

application = Flask(__name__)
application.debug = True

@application.route('/')
def index():
    return "Sup G"

