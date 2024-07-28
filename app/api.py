from flask import Flask, render_template, Blueprint

api = Blueprint('api', __name__, template_folder='templates')

app = Flask(__name__)


@api.route('/')
def index():
    return render_template('index.html')


@api.route('/about')
def about():
    return render_template('about.html')
