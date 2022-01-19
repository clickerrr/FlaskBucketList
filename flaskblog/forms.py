from wtforms import Form, StringField, BooleanField, PasswordField, SubmitField, validators, TextAreaField

class RegistrationForm(Form):
    username = StringField(label="Username", validators=[validators.DataRequired(), validators.Length(min=4, max=20)])
    password = PasswordField(label="Password", validators=[validators.DataRequired()])
    repeat_password = PasswordField(label="Repeat Password",
                                    validators=[validators.DataRequired(),
                                                validators.EqualTo(fieldname="password", message="Passwords Must Match")])
    email = StringField(label="Email", validators=[validators.DataRequired(), validators.Email()])
    submit = SubmitField(label="Submit")

class LoginForm(Form):
    username_or_email = StringField(label="Username/Email", validators=[validators.DataRequired()])
    password = PasswordField(label="Password", validators=[validators.DataRequired()])
    remember = BooleanField(label="Remember Me")
    submit = SubmitField(label="Submit")

class NewPostForm(Form):
    title = StringField(label="Enter Your Title", validators=[validators.DataRequired(), validators.length(min=1, max=32)])
    content = TextAreaField(label="Enter Your Content", validators=[validators.DataRequired(), validators.length(min=1, max=300, message="Content Can Not Be Blank")])
    submit = SubmitField(label="Submit")