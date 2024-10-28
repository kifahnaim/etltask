Project Setup Instructions
Clone the Repository:

git clone https://github.com/kifahnaim/etltask.git
cd etltask
Create a Virtual Environment: If you haven't already, create a virtual environment to isolate your project dependencies:

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install Dependencies: Make sure you have requirements.txt in your project directory. If it exists, install the dependencies:

pip install -r requirements.txt
Configure Database: Update your settings.py file to configure the PostgreSQL database. Ensure the following parameters are correctly set:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
Run Migrations: After setting up the database, apply migrations:
python manage.py migrate
Create a Superuser (optional, for accessing the admin):

python manage.py createsuperuser
Running the ETL Process
Locate the ETL Script: Ensure you have the Python script for the ETL process (e.g., etl_script.py).

Run the ETL Process: Execute the ETL script:
python etl_script.py
This script should read, apply basic transformations, and load data into PostgreSQL.

Running the Application
Start the Django Development Server: Run the following command to start the server:

python manage.py runserver
Access the Application: Open your browser and navigate to http://127.0.0.1:8000/.

API Access Instructions
Accessing the APIs:

Transactions API:
GET http://127.0.0.1:8000/api/transactions/1/?date=2024-10-23
Query Parameter: date (format: YYYY-MM-DD)
Authentication: Requires a JWT token.
Transaction Summary API:

GET http://127.0.0.1:8000/api/transaction_summary/1/
Reads from the materialized view.
Authentication: To access APIs that require JWT authentication, you need to:

Obtain a JWT token by authenticating (usually through a login API).
Include the token in the request headers:
Authorization: Bearer <your_jwt_token>
Example of Using the APIs with cURL
Get Transactions:

curl -H "Authorization: Bearer <your_jwt_token>" "http://127.0.0.1:8000/api/transactions/1/?date=2024-10-23"
Get Transaction Summary:

curl -H "Authorization: Bearer <your_jwt_token>" "http://127.0.0.1:8000/api/transaction_summary/1/"
