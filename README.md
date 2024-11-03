## 📚 Table of Contents
- [Introduction](#Introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup Instructions](#setup-instructions)
- [File Structure](#file-structure)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## 🌟 Introduction

**Future Auth** is a web application that provides user authentication features using Firebase. It allows users to sign up, sign in, and manage their sessions with a modern and responsive design. The application supports light and dark themes, enhancing user experience.

## ✨ Features

- 🔒 User registration and authentication
- 📅 Session management
- 🌈 Responsive design with light and dark themes
- 📝 Flash messages for user feedback
- 🛠️ Built with Flask and Firebase

## 💻 Technologies Used

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python, Flask
- **Database**: Firebase
- **Environment Management**: Virtualenv
- **Package Management**: pip

## ⚙️ Setup Instructions

### Prerequisites

- Python 3.12 or higher
- pip (Python package installer)
- Firebase account and project setup

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/future-auth.git
   cd future-auth
   ```

2. **Run the setup script**:
   - For Windows:
     ```bash
     setup.bat
     ```
   - For macOS/Linux:
     ```bash
     bash setup.sh
     ```

3. **Create a Firebase service account**:
   - Go to your Firebase project settings.
   - Generate a new private key for your service account and save it as `firebase_key.json` in the project root.

4. **Run the application**:
   - For Windows:
     ```bash
     run.bat
     ```
   - For macOS/Linux:
     ```bash
     bash run.sh
     ```

## 📁 File Structure

```
future-auth/
│
├── app.py                  # Main application file
├── firebase_key.json       # Firebase service account key
├── requirements.txt        # Python dependencies
├── run.bat                 # Windows script to run the app
├── run.sh                  # Bash script to run the app
├── setup.bat               # Windows script to set up the environment
├── setup.sh                # Bash script to set up the environment
├── static/                 # Static files (CSS, JS)
│   ├── script.js           # JavaScript for theme toggle
│   └── styles.css          # CSS styles for the application
└── templates/              # HTML templates
    ├── base.html           # Base template
    ├── home.html           # Home page template
    ├── login.html          # Login page template
    └── signup.html         # Signup page template
```

## 🛠️ Usage

- **Home Page**: Displays a welcome message and options to sign in or sign up.
- **Sign In**: Users can log in with their email and password.
- **Sign Up**: New users can create an account.
- **Theme Toggle**: Users can switch between light and dark themes.

## 🤝 Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any improvements or features.

---
