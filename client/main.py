from flask import Blueprint, render_template

mainRoute = Blueprint('main',__name__,template_folder='pages',static_url_path='',static_folder='static')

@mainRoute.route('/')
def home():
    return render_template('home.html')

@mainRoute.route('/events')
def events():
    return render_template('events.html')

@mainRoute.route('/tags')
def tags():
    return render_template('tags.html')

@mainRoute.route('/settings')
def settings():
    return render_template('setings.html')

@mainRoute.route('/profile')
def profile():
    return render_template('profile.html')