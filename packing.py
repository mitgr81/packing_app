from flask import Flask, render_template

application = Flask(__name__)
application.debug = True


@application.route('/')
@application.route('/<beans>')
def index(beans=None):
    return render_template('index.html', beans=beans)

if __name__ == '__main__':
    application.run(debug=True)
