from flask import Flask, render_template

application = Flask(__name__)


@application.route('/')
@application.route('/<list_id>')
def index(list_id=None):
    return render_template('index.html', title=list_id or 'Manager')

@application.route('/create')
def create_list():
    return render_template('create_list.html')

if __name__ == '__main__':
    application.run(debug=True)
