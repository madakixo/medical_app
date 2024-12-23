# medical_app
developing app to sort medication based on symptoms
# Medical Symptom Database App

This Flask application serves as a backend for managing and querying a medical symptom database. Here's a detailed guide on how to set it up and run it on your local machine.

## Prerequisites

- **Python**: Version 3.8 or later. Check your version with:
  ```bash
  python --version


  Git: For cloning the repository.
SQLite: Comes bundled with Python, but you can use any SQL database supported by SQLAlchemy.
A text editor or IDE: For writing and editing code (e.g., VSCode, PyCharm).

Installation Guide
Step 1: Clone the Repository
Clone this repository to your local machine:

bash
git clone <your-repository-url>
cd medical-symptom-database-app

Step 2: Set Up Virtual Environment
Using a virtual environment isolates your project dependencies:

bash
python -m venv venv

Activate the virtual environment:

On macOS and Linux:
bash
source venv/bin/activate
On Windows:
bash
venv\Scripts\activate

Step 3: Install Dependencies
Install the required Python packages listed in requirements.txt:

bash
pip install -r requirements.txt

Step 4: Configure the Application
Environment Variables: 
Create a .env file in the project's root directory for sensitive configurations:
SQLALCHEMY_DATABASE_URI=sqlite:///medical_symptom.db
SECRET_KEY=your-secret-key-here  # Used for sessions, forms, etc.
# Add any other environment variables here
If you're using a different database than SQLite, adjust the SQLALCHEMY_DATABASE_URI accordingly.

Step 5: Database Setup
Initialize Migrations:
Flask-Migrate manages your database schema changes. Start by initializing migrations:
bash
flask db init
Generate Initial Migration:
After setting up your models (in app/models.py), create an initial migration:
bash
flask db migrate -m "Initial migration"
Apply Migrations:
Apply the generated migrations to create or update your database:
bash
flask db upgrade

Step 6: Populate Database (Optional)
If you have seed data or scripts to populate your database:
Run your seed script, if one exists:
bash
python seed.py  # Assuming you have a script named seed.py

Step 7: Run the Application
Start the Flask application:
bash
flask run --app app:create_app

Or if you have a run.py:
bash
python run.py
By default, your app will run on http://127.0.0.1:5000/. Adjust the --host or --port if needed, especially if you're running on different machines or need to test from another device:
bash
flask run --app app:create_app --host=0.0.0.0 --port=5000

Step 8: Testing
Ensure you have tests set up. If you're using pytest:
bash
pytest tests/

Step 9: Development Tips
Debug Mode: Use --debug for development:
bash
flask run --debug --app app:create_app
Environment: Use .flaskenv for setting FLASK_ENV=development automatically.
Logging: Check your application logs for debugging or ensuring everything runs smoothly.

Troubleshooting
Database Errors: Ensure your database file exists or you have the correct permissions for creating it.
Dependency Issues: If you encounter issues with package installations, try updating pip:
bash
pip install --upgrade pip
Migration Problems: If migrations fail, check your model definitions and ensure they match your intended schema.

Notes
Production: The built-in Flask server is not suitable for production. 
Use Gunicorn or uWSGI for a WSGI server and consider using a reverse proxy like Nginx or Apache.
Security: Always secure your application with HTTPS, CSRF protection, and proper user authentication in production environments.

