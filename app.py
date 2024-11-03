from flask import Flask, render_template, request, redirect, url_for, flash, session
import firebase_admin
from firebase_admin import credentials, auth
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Initialize Firebase Admin SDK
cred = credentials.Certificate("firebase_key.json")
firebase_admin.initialize_app(cred)

@app.route('/')
def home():
    user = session.get('user')
    return render_template('home.html', user=user)

@app.route('/login', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            user = auth.get_user_by_email(email)
            # In a real application, you should verify the password here
            # For demonstration purposes, we're just checking if the user exists
            session['user'] = {'email': user.email}
            flash('Signed in successfully!', 'success')
            return redirect(url_for('home'))
        except auth.AuthError as e:
            flash(f'Error loging in: {str(e)}', 'error')
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            user = auth.create_user(email=email, password=password)
            session['user'] = {'email': user.email}
            flash('Account created successfully!', 'success')
            return redirect(url_for('home'))
        except auth.AuthError as e:
            flash(f'Error creating account: {str(e)}', 'error')
    return render_template('signup.html')

@app.route('/signout')
def signout():
    session.pop('user', None)
    flash('Signed out successfully!', 'success')
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)