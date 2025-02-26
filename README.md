Meerut Zone

Meerut Zone is a web application built using Django (Python 3.10) to explore the city of Meerut. This platform provides details about places, events, restaurants, historical sites, and other attractions in Meerut.

Features

Explore Places: View and search for popular attractions, historical sites, and local businesses.

Events & Activities: Find upcoming events and activities in Meerut.

Restaurant Listings: Discover restaurants and their specialties.

User Reviews & Ratings: Leave and read reviews for different places.

Interactive Map: Locate places with integrated map functionality.

Admin Panel: Manage places, events, and users through a Django admin interface.

Technologies Used

Backend: Django (Python 3.10), Django REST Framework

Frontend: HTML, CSS, JavaScript (or React if applicable)

Database: PostgreSQL / SQLite

Authentication: Django Authentication System

Deployment: AWS EC2 / DigitalOcean / Heroku

Installation & Setup

Prerequisites

Ensure you have the following installed:

Python 3.10+

pip (Python package manager)

virtualenv (Recommended for managing dependencies)

PostgreSQL (or SQLite for local development)

Step 1: Clone the Repository

git clone git@github.com:your-username/meerut_zone.git
cd meerut_zone

Step 2: Set Up a Virtual Environment

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Step 3: Install Dependencies

pip install -r requirements.txt

Step 4: Configure Database

Using SQLite (Default for Development)

No additional setup is needed.

Using PostgreSQL (For Production)

Install PostgreSQL and create a database.

Update settings.py with your database credentials.

Step 5: Run Migrations

python manage.py migrate

Step 6: Create a Superuser (Admin Panel)

python manage.py createsuperuser

Enter the required details.
Step 7: Start the Development Server
python manage.py runserver
Access the project at: http://127.0.0.1:8000/

