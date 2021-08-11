from flask_babel import lazy_gettext as _l
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError

from app.models import User

class LoginForm(FlaskForm):
    username = StringField(_l('Имя'), validators=[DataRequired()])
    password = PasswordField(_l('Пароль'), validators=[DataRequired()])
    remember_me = BooleanField(_l('Запомни меня'))
    submit = SubmitField(_l('Войти'))


class RegistrationForm(FlaskForm):
    username = StringField(_l('Имя'), validators=[DataRequired()])
    email = StringField(_l('Email'), validators=[DataRequired(), Email()])
    password = PasswordField(_l('Пароль'), validators=[DataRequired()])
    password2 = PasswordField(_l('Повторите пароль'), 
                              validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField(_l('Регистрация'))

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError(_l('Это имя уже занято'))

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError(_l('Эта почта уже используется'))


class EditProfileForm(FlaskForm):
    username = StringField(_l('Имя'), validators=[DataRequired()])
    about_me = TextAreaField(_l('О себе'), validators=[Length(min=0, max=140)])
    submit = SubmitField(_l('Отправить'))

    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username
    
    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidationError(_l('Это имя уже занято'))


class PostForm(FlaskForm):
    post = TextAreaField(_l('Скажите что-нибудь:'), validators=[
        DataRequired(), Length(min=1, max=140)])
    submit = SubmitField(_l('Отправить'))


class ResetPasswordRequestForm(FlaskForm):
    email = StringField(_l('Email'), validators=[DataRequired(), Email()])
    submit = SubmitField(_l('Запросить сброс пароля'))


class ResetPasswordForm(FlaskForm):
    password = PasswordField(_l('Пароль'), validators=[DataRequired()])
    password2 = PasswordField(_l('Повторите пароль'), 
                              validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField(_l('Сбросить пароль'))