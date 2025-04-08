Quora-Inspired Website (Django Assignment)

Follow these steps to set up and run the project on your local machine:

1. **Prerequisites:**
    * Python 3.x installed on your system.
    * pip (Python package installer) installed.

2.  **Clone the Repository:**
    * git clone <YOUR_REPOSITORY_URL>
    * cd <YOUR_PROJECT_DIRECTORY>

3. **Create and Activate a Virtual Environment (Recommended):**
    * python -m venv venv
    * source venv/bin/activate #  On MacOs/Linux
    * venv\Scripts\activate # On Windows

4. **Install Dependencies:**
    * pip install -r requirements.txt

5. **Apply Migrations:**
   * python manage.py makemigrations <app_name>
   * python manage.py migrate 
   * This will create the necessary database tables for your Django application.

6. **Run the Development Server:**
    * python manage.py runserver

7.  **Access the Website:**
    * Open your web browser and navigate to `http://127.0.0.1:8000/`.


## Functionality

The website provides the following core features:

**User Authentication:**
    * Users can create new accounts through a registration form.
    * Registered users can log in and log out of their accounts.

**Question Management:**
    * Logged-in users can post new questions.
    * All posted questions are visible to all users.

**Answer Management:**
    * Logged-in users can answer questions posted by others.
    * Answers are displayed below their respective questions.

**Liking Answers:**
    * Logged-in users can like answers provided by others.
    * The number of likes for each answer is displayed.

## Project Structure

quora_project/
├── quora_app/
│   ├── migrations/
│   │   └── ...
│   ├── templates/
│   │   └── login.html
│   │   └── base.html
│   │   └── question_detail.html
│   │   └── question_list.html
│   │   └── registration.html
│   │   └── ask_question.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── quora_project/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3
├── manage.py
└── Readme.md


## Key Implementation Details

* **Models:** Define the database structure for users, questions, answers, and likes.
* **Forms:** Django Forms are used for handling user input for registration, login, posting questions, and submitting answers.
* **Views:** Django views handle the application logic, interacting with the models and forms to process user requests and render templates.
* **URLs:** URL patterns map web addresses to your Django views.
* **Templates:** Basic HTML templates are used to display data to the user and provide interactive elements (forms, links, etc.).
