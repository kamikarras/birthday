from flask import Flask, render_template, redirect, request, flash, session, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc
from model import User, app, Comment, connect_to_db, db
from jinja2 import StrictUndefined
from sqlalchemy.orm import relationship




app = Flask(__name__)

app.secret_key = "ABC"

@app.route('/')
def show_home():
    """shows the hompage"""

    return render_template("homepage.html")


@app.route('/register', methods=["GET"])
def show_registration():
    """shows the registration form"""

    return render_template("register.html")


@app.route('/register', methods=["POST"])
def register_user():
    """adds user to database"""

    # get email and password for new user from form
    email = request.form['email']
    fullname = request.form['fullname']
    password = request.form['password']
    new_user = User(fullname=fullname, email=email, password=password, rsvp='undeclared')

    # add the user to the user database
    db.session.add(new_user)
    db.session.commit()

    return redirect("/")

@app.route('/login', methods=['GET'])
def login_form():
    """shows the login form"""

    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_process():

    # get user details from form
    email = request.form['email']
    password = request.form['password']

    # query to get user from database
    user = User.query.filter_by(email=email).first()

    # check if this is a user and if the password matchs
    if not user:
        flash("no such user")
        return redirect('/login')

    if user.password != password:
        flash("Password does not match.")
        return redirect('/login')

    session["user_id"] = user.user_id

    flash('You are logged in')
    return redirect(f"/profile/{user.user_id}")

@app.route('/profile/<int:user_id>', methods=['GET'])
def view_profile(user_id):
    """shows the user profile"""

    user_id = session.get("user_id")
    user = User.query.filter_by(user_id=user_id).first()
    fullname = user.fullname

    return render_template('profile.html',
                            fullname=fullname,
                            user_id=user_id)



if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True
    # make sure templates, etc. are not cached in debug mode
    app.jinja_env.auto_reload = app.debug

    connect_to_db(app)

    app.run(port=5000, host='0.0.0.0')
