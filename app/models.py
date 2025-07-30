from datetime import datetime
from .extensions import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id: int = db.Column(db.Integer, primary_key=True)
    username: str = db.Column(db.String(80), unique=True, nullable=False)
    email: str = db.Column(db.String(120), unique=True, nullable=False)
    password_hash: str = db.Column(db.String(128), nullable=False)
    created_at: datetime = db.Column(db.DateTime, default=datetime.utcnow)
    notes = db.relationship('Note', backref='user', lazy=True)
    folders = db.relationship('Folder', backref='user', lazy=True)

class Folder(db.Model):
    id: int = db.Column(db.Integer, primary_key=True)
    name: str = db.Column(db.String(100), nullable=False)
    user_id: int = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created_at: datetime = db.Column(db.DateTime, default=datetime.utcnow)
    notes = db.relationship('Note', backref='folder', lazy=True)

class Note(db.Model):
    id: int = db.Column(db.Integer, primary_key=True)
    title: str = db.Column(db.String(200), nullable=False)
    content: str = db.Column(db.Text, nullable=False)
    folder_id: int = db.Column(db.Integer, db.ForeignKey('folder.id'), nullable=True)
    user_id: int = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created_at: datetime = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at: datetime = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow) 