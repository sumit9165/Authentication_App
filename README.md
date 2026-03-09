# Authentication_App
# Django Authentication App

A Django-based authentication system with email functionality using Mailtrap.

---

# Requirements

Before running this project, make sure you have the following installed:

* Python 3.10+
* pip
* virtualenv (recommended)
* Git

Check Python version:

```bash
python --version
```

---

# Project Setup

## 1. Clone the Repository

```bash
git clone https://github.com/yourusername/authentication_app.git
cd authentication_app
```

---

# Create Virtual Environment

Create a virtual environment:

```bash
python -m venv venv
```

Activate it.

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables (.env)

Create a `.env` file in the **project root directory**.

Example:

```env
SECRET_KEY=your_django_secret_key
DEBUG=True

# Database (example for sqlite)
DB_NAME=db.sqlite3

# Mailtrap Email Configuration
EMAIL_HOST=sandbox.smtp.mailtrap.io
EMAIL_HOST_USER=your_mailtrap_username
EMAIL_HOST_PASSWORD=your_mailtrap_password
EMAIL_PORT=2525
EMAIL_USE_TLS=True
DEFAULT_FROM_EMAIL=hello@example.com
```

---

# Mailtrap Setup

1. Go to:

```
https://mailtrap.io
```

2. Create an account.

3. Go to **Email Testing → SMTP Settings**

4. Copy credentials and paste them in `.env`.

Example credentials:

```env
EMAIL_HOST=sandbox.smtp.mailtrap.io
EMAIL_HOST_USER=123456789
EMAIL_HOST_PASSWORD=abcdef123456
EMAIL_PORT=2525
EMAIL_USE_TLS=True
```

---

# Apply Database Migrations

Run the following commands:

```bash
python manage.py makemigrations
```

```bash
python manage.py migrate
```

---

# Create Superuser

```bash
python manage.py createsuperuser
```

Follow the prompts to create an admin account.

---

# Run the Development Server

```bash
python manage.py runserver
```

Server will start at:

```
http://127.0.0.1:8000/
```

---

# Access Admin Panel

Open:

```
http://127.0.0.1:8000/admin
```

Login using the superuser credentials.

---

# Project Structure

```
project_root/
│
├── authentication_app/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── manage.py
├── requirements.txt
├── .env
└── README.md
```

---

# Useful Django Commands

Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

Create superuser

```bash
python manage.py createsuperuser
```

Run development server

```bash
python manage.py runserver
```

Collect static files (production)

```bash
python manage.py collectstatic
```

---

# Notes

* Never commit the `.env` file to GitHub.
* Add `.env` to `.gitignore`.

Example `.gitignore` entry:

```
.env
venv/
__pycache__/
db.sqlite3
```

---

# License

This project is licensed under the MIT License.
