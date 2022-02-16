from website import db, login_manager
from datetime import datetime
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    name = db.Column(db.String(20), nullable=False)
    backref = db.relationship('Sample Backref', backref='author', lazy=True)

# sets print settings for the model
    def __repr__(self):
        return f"User('{self.username}','{self.image_file}')"

class SampelModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sample_string = db.Column(db.String(100), nullable=False)
    sample_int = db.Column(db.Integer)
    sample_datetime = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    sample_text = db.Column(db.Text)
    sample_user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)