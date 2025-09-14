from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from twitterflask.models import User

class RegistrationForm(FlaskForm):
    username = StringField('Nome de usuário', validators=[DataRequired(), Length(min=2, max=25)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Senha',validators=[DataRequired()])
    confirm_password = PasswordField('Confirmar Senha',validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Registrar-se')

    def validate_username(self, username):

        user = User.query.filter_by(username=username.data).first()

        if user:
            raise ValidationError('Usuário já existente.')
    
    def validate_email(self, email):

        user = User.query.filter_by(email=email.data).first()

        if user:
            raise ValidationError('Email já usado.')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Senha',validators=[DataRequired()])
    remember = BooleanField('Mantenha-me conectado')
    submit = SubmitField('Log In')