from flask import render_template, redirect, url_for, request, flash, jsonify
from flaskblog import app, database, login
from flaskblog.forms import RegistrationForm, LoginForm, NewPostForm
from flaskblog.db import User, Posts
from flask_login import login_required, logout_user, login_user, current_user
from werkzeug.security import generate_password_hash

# route for the default index
@app.route("/home", methods=["GET", "POST"])
@login_required
def index():
    if current_user.is_authenticated:
        posts = Posts.query.filter_by(user_rel=current_user)

    flaskNewPostForm = NewPostForm(request.form)
    if request.method == "POST" and flaskNewPostForm.validate():
        new_post = Posts(title=str(flaskNewPostForm.title.data), content=str(flaskNewPostForm.content.data), user_rel=current_user)
        database.session.add(new_post)
        database.session.commit()
        return redirect(url_for("index"))

    return render_template("index.html", posts=posts, newPostForm=flaskNewPostForm)

@app.route("/showSignUp", methods=["GET", "POST"])
def signUpPage():
    flaskRegForm = RegistrationForm(request.form)
    if request.method == 'POST':
        if flaskRegForm.validate():
            user_exists = User.query.filter_by(username=str(flaskRegForm.username.data)).first()
            if user_exists:
                flash("User already exists")
            else:
                user_exists = User.query.filter_by(email=str(flaskRegForm.email.data)).first()
                if user_exists:
                    flash("Email already registered")
                else:
                    user = User(username=str(flaskRegForm.username.data), email=str(flaskRegForm.email.data),
                                password_hash=str(flaskRegForm.password.data))
                    user.hashPassword(user.password_hash)

                    database.session.add(user)
                    database.session.commit()
                    login_user(user, remember=False)
                    return redirect(url_for("index"))

    return render_template("signup.html", regForm=flaskRegForm)

@app.route("/", methods=["GET", "POST"])
def signInPage():

    if current_user.is_authenticated:
        return redirect(url_for("index"))

    flaskLoginForm = LoginForm(request.form)
    if request.method == 'POST' and flaskLoginForm.validate():
        is_user = User.query.filter_by(username=str(flaskLoginForm.username_or_email.data)).first()
        if is_user:
            is_password = is_user.checkPasswordHash(password=str(flaskLoginForm.password.data))
            if is_user and is_password:
                login_user(user=is_user)
                flash("Logged in successfully")
                return redirect(url_for('index'))
            else:
                flash("Incorrect Username or Password")
        else:
            is_user = User.query.filter_by(email=str(flaskLoginForm.username_or_email.data)).first()
            if is_user:
                is_password = is_user.checkPasswordHash(password=str(flaskLoginForm.password.data))
                if is_user and is_password:
                    is_user
                    login_user(user=is_user)
                    flash("Logged In Successfully")
                    return redirect(url_for('index'))
                else:
                    flash("Incorrect Username or Password")
            else:
                flash("Incorrect username or password")

    return render_template("signin.html", loginForm=flaskLoginForm)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("signInPage"))

@app.route("/removePost", methods=['POST'])
def removePost():
    if request.method == "POST":
        try:
            data = request.get_json(force=True)["data"]
            query_post = Posts.query.filter_by(id=data).first()
            if query_post:
                database.session.delete(query_post)
                database.session.commit()
            else:
                raise Exception("Post Does Not Exist")
        except Exception as e:
            print("error: " + str(e))
    return "OK"

@app.route("/newPost", methods=['POST'])
def addPost():
    try:
        title = request.get_json(force=True)["title"]
        content = request.get_json(force=True)["content"]
        if current_user:
            new_post_to_commit = Posts(title=str(title), content=str(content), user_rel=current_user)
            database.session.add(new_post_to_commit)
            database.session.commit()
            postId = Posts.query.filter_by(title=str(title), content=str(content)).order_by(Posts.id.desc()).first().id
            print("ADDING: " + str(postId))
            return jsonify({'id': postId})
        else:
            raise Exception("Current User Error")
    except Exception as e:
        print("error: " + str(e))
    return "Ok"

@login.unauthorized_handler
def unauthorized():
    # do stuff
    flash("Please login to access this page")
    return redirect(url_for("signInPage"))