from flask import render_template, redirect, url_for, flash, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from . import auth_bp
from ..extensions import db
from ..models import User

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username_or_email = request.form.get('username').strip()
        password = request.form.get('password')
        user = User.query.filter((User.username == username_or_email) | (User.email == username_or_email)).first()
        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            flash('Logged in successfully.', 'success')
            return redirect(url_for('main.home'))
        else:
            flash('Invalid username/email or password.', 'danger')
    return render_template('auth/login.html')

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username').strip()
        email = request.form.get('email').strip().lower()
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        # Validation
        if not username or not email or not password or not confirm_password:
            flash('All fields are required.', 'danger')
        elif password != confirm_password:
            flash('Passwords do not match.', 'danger')
        elif User.query.filter_by(username=username).first():
            flash('Username already exists.', 'danger')
        elif User.query.filter_by(email=email).first():
            flash('Email already registered.', 'danger')
        else:
            hashed_pw = generate_password_hash(password)
            user = User(username=username, email=email, password_hash=hashed_pw)
            db.session.add(user)
            db.session.commit()
            flash('Registration successful! You can now log in.', 'success')
            return redirect(url_for('auth.login'))
    return render_template('auth/register.html')

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('main.home')) 