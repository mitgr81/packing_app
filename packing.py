from flask import Flask, render_template, flash

application = Flask(__name__)
application.secret_key = "banana sandwich donkey shoe"


@application.route('/')
@application.route('/<list_id>')
def index(list_id=None):
    return render_template('index.html', title=list_id or 'Manager')


@application.route('/create', methods=['GET'])
def show_create_list_form():
    return render_template('create_list.html')


@application.route('/create', methods=['POST'])
def post_list():
    flash("Your list has been saved")
    return render_template('index.html', title="List Created")

if __name__ == '__main__':
    application.run(debug=True)
