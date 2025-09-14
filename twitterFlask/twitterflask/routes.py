from flask import render_template, url_for, flash, redirect, request
from twitterflask import app, db, bcrypt
from twitterflask.forms import RegistrationForm, LoginForm
from twitterflask.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Tweet 1',
        'content': 'Primeiro conteúdo postado',
        'date_posted': '20 de abril de 2025'
    },
    {
        'author': 'Gabriel Salerno',
        'title': 'Tweet 2',
        'content': 'Segundo conteúdo postado',
        'date_posted': '21 de abril de 2025'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='Sobre')

@app.route("/register", methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data,email=form.email.data,password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Sua conta foi criada! Você já consegue logar.','success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Registrar-se', form=form)

@app.route("/login", methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Erro no login. Por favor checar o email e/ou a senha.', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route("/account")
@login_required
def account():
    return render_template('account.html', title='Conta')