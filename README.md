# Hack the North backend challenge

# Project Summary:

This Django application is designed for managing participants and their associated skills, particularly useful for hackathons or similar events. It features CRUD operations on participants, skills management, and an endpoint for listing skills with the ability to filter based on frequency.

# Database:

In a typical scenario like a hackathon, a single participant can have multiple skills (e.g., Python, Django, JavaScript). Also, a single skill can be associated with multiple participants, each with a unique skill rating. Thus, I designed the data model to be many-to-many, where separate tables for participants and skills are created, with an additional junction table called participant skills which additionally stores the rating.

# Installation:

**Prerequisites**

Before you begin, ensure you have Python 3.x installed on your system.

**Clone the Repository**


```
git clone https://github.com/yourusername/django-participants-skills.git
cd django-participants-skills
```
Setup Virtual Environment

```
python -m venv venv
```
**Activate it on Windows**
```
venv\Scripts\activate
```
**Or on Unix/MacOS**
```
source venv/bin/activate
```
**Install Dependencies**

```
pip install -r requirements.txt
```

**Database Migrations**

Initialize the database using Django's built-in migrate command

```
python manage.py migrate
```

**Create an Admin User**

To access the admin panel, create an admin user.

```
python manage.py createsuperuser
```

**Run the Development Server**
```
python manage.py runserver
```
Visit http://127.0.0.1:8000/ in your browser to see the application. to see the admin page, go to http://127.0.0.1:8000/admin to see the database tables.

# Endpoints:

**List All Users**
- Endpoint: GET /users/

- Example: ```http://localhost:8000/users/```

- Description: Retrieves a list of all participants in the system.

- Parameters: None

- Response: A JSON array of participants, each with their respective details.


**Get User Details:**

- Endpoint: GET /users/<int:pk>/

- Example: ```http://localhost:8000/users/2``` gets user with id of 2

- Description: Fetches details of a specific participant by their unique ID (pk).

- Parameters: pk (path parameter) - The unique identifier of the participant.

- Response: A JSON object containing details of the specified participant.

**Update User Details:**

- Endpoint: PUT /users/<int:pk>/update/

- Example: ```http://localhost:8000/users/1/update/``` update for user with id 1
  
- Example request body:
 ```
   {
    "phone": "+1 (555) 123 4567"
  }
```

- Description: Updates the details of a specific participant. This endpoint expects all participant fields to be provided in the request body.

Parameters:

- pk (path parameter) - The unique identifier of the participant.

- Request body - A JSON object representing the updated fields for the participant.

- Response: A JSON object containing the updated details of the participant.

**Frequency of Skills:**

- Endpoint: ```GET /skills/```

- Example: ```http://localhost:8000/skills/?min_frequency=1&max_frequency=15```

- Description: Retrieves a list of all skills available in the system.

- Parameters: None 

- Response: A JSON array of skills.
