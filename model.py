from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import load_only, relationship

db = SQLAlchemy()


class User(db.Model):
    """user Model"""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fullname = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(64), nullable=False)
    password = db.Column(db.String(64), nullable=False)
    rsvp = db.Column(db.String(64), nullable=False)

    def __repr__(self):
        """displays user"""

        return f"""<User
                    user_id={self.user_id}
                    fullname={self.fullname}
                    email={self.email}"""


class Comment(db.Model):
    """comment model"""

    __tablename__ = "comments"

    comment_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    comment = db.Column(db.String(160), nullable=False)
    date_posted = db.Column(db.Date, nullable=False)

    user = db.relationship('User', backref=db.backref('users', order_by=user_id))



def connect_to_db(app):
    """Connect to database."""

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///birthday'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)                    


app = Flask(__name__)

if __name__ == "__main__":
    connect_to_db(app)
    # load_jobs()
    # load_skills()
    # load_job_skill_counts()
    db.create_all()
