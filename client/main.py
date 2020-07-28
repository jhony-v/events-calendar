from flask import Blueprint, render_template

mainRoute = Blueprint('main',__name__,template_folder='pages')

@mainRoute.route('/')
def home():
    return render_template('home.html')