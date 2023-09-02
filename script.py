import os
import django

# Configure Django settings manually
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "meritsystem.settings")  # Replace with your actual project name

# Initialize Django
django.setup()
import sqlite3
import random
from faker import Faker
from django.contrib.auth.hashers import make_password  # Import Django's make_password function
from datetime import datetime  # Import the datetime module

fake = Faker()

# Connect to your SQLite database
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

# Generate and insert random records
for _ in range(100):  # Adjust the number of records as needed
    first_name = fake.first_name()
    last_name = fake.last_name()
    email = fake.email()  # Generate a random email address
    grade = random.randint(0, 12)  # Random grade between 0 and 12

    # Get the current date and time
    date_joined = datetime.now()

    # Generate a random password
    password = "azamat123"

    # Use Django's make_password to hash the password
    hashed_password = make_password(password)

    # Insert into User table with random email, hashed password, is_superuser=0, is_staff=0, is_active=1, and date_joined=current date and time
    cursor.execute('''
        INSERT INTO auth_user (username, first_name, last_name, email, password, is_superuser, is_staff, is_active, date_joined)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (fake.user_name(), first_name, last_name, email, hashed_password, 0, 0, 1, date_joined))

    # Get the last inserted user_id
    user_id = cursor.lastrowid

    # Insert into UserExtension table
    cursor.execute('''
        INSERT INTO main_userextention (grade, user_id)
        VALUES (?, ?)
    ''', (grade, user_id))

# Commit changes and close the connection
conn.commit()
conn.close()

print("Random records with hashed passwords, random email addresses, active status, and date joined have been inserted into the SQLite database.")
