from flask import Flask, request, make_response, redirect, render_template, session, url_for, flash
from flask_bootstrap import  Bootstrap
import unittest
from app import createApp
from app.forms import LoginForm

app = createApp()


TODOS = ['TODO 1', 'TODO 2', 'TODO 3', 'TODO 4' ]


@app.cli.command()
def test():
    test = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(test)

@app.errorhandler(404)
def not_found_400(error):
    return render_template('404.html', error=error)

@app.errorhandler(500)
def not_found_500(error):
    return render_template('500.html', error=error)

@app.route('/')
def index():
    user_ip = request.remote_addr
    response = make_response(redirect('/hello'))
    session['user_ip'] = user_ip
    return response

@app.route('/hello', methods=['GET', 'POST'])
def hello():
    user_ip = session.get('user_ip')
    login_form = LoginForm()
    user_name = session.get('user_name')

    context = {
        'user_ip' : user_ip,
        'TODOS' : TODOS,
        'login_form': login_form,
        'user_name': user_name
        }

        #Escucha del evento submit
    if login_form.validate_on_submit():
        user_name = login_form.user_name.data
        session['user_name'] = user_name
        #Mensaje emergente
        flash('Nombre de usuario registrado con éxito!')
        return redirect(url_for('index'))

    return render_template('hello.html',  **context)

