# routes.py
from flask import render_template, flash, redirect, url_for, session
from app import app
from app.forms import LoginForm 

@app.route("/")
@app.route("/home")
def index():
    return render_template('home.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Login request for {form.username.data}, remember me ={form.remember_me.data}', category='info')
        user = {'username': form.username.data}
        session['user'] = user
        return redirect(url_for('index'))
    return render_template('login.html', form=form)