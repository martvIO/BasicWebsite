from flask import Flask, render_template, request, redirect, url_for, flash, session
import firebase_admin
from firebase_admin import credentials, auth

# Initialize Flask app
app = Flask(__name__)
app.secret_key = "your_secret_key"

# Initialize Firebase Admin SDK
cred = credentials.Certificate("firebase_key.json")
firebase_admin.initialize_app(cred)

# Route for Home page
@app.route('/')
def home():
    # Check if the user is logged in by seeing if 'user_email' is in session
    user_email = session.get('user_email')
    return render_template('home.html', user_email=user_email)

# Route for Login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            # Check if the user exists (and ideally validate the password)
            user = auth.get_user_by_email(email)
            # Store the user's email in the session to keep them logged in
            session['user_email'] = email
            flash('Logged in successfully!', 'success')
            print("User login was successful!")
            return redirect(url_for('home'))
        except:
            flash('Login failed. Please check your credentials.', 'danger')
            print("Login attempt was unsuccessful")
    return render_template('login.html')

# Route for Signup page
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            # Create a new user in Firebase Authentication
            user = auth.create_user(email=email, password=password)
            flash('Account created successfully!', 'success')
            return redirect(url_for('login'))
        except:
            flash('Account creation failed. Try again.', 'danger')
    return render_template('signup.html')

# Route for Logout
@app.route('/logout')
def logout():
    # Clear the session to log out the user
    session.pop('user_email', None)
    flash('You have been logged out.', 'info')
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
