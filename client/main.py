from flask import Blueprint, render_template

mainRoute = Blueprint('main',__name__,template_folder='pages',static_url_path='',static_folder='static')

@mainRoute.route('/')
def home():
    return render_template('home.html')