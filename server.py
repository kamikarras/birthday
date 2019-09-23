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



if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True
    # make sure templates, etc. are not cached in debug mode
    app.jinja_env.auto_reload = app.debug

    connect_to_db(app)

    app.run(port=5000, host='0.0.0.0')
