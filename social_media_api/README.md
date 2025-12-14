Objective: Start building a Social Media API from scratch, focusing on setting up the project environment, user authentication, and creating the initial user models.

Task Description:
Begin by establishing the foundational elements of your Social Media API. This includes setting up the Django project, integrating Django REST Framework for API functionality, and implementing a robust user authentication system.

# Step 1: Create a New Django Project
## Environment Setup:
```bash
done
``` 
Install Django and Django REST Framework using pip, if not already installed: bash pip install django djangorestframework
Create a new Django project named social_media_api: bash django-admin startproject social_media_api
Navigate into your project directory and create a new Django app called accounts for handling user-related functionality: bash cd social_media_api python manage.py startapp accounts
Add 'rest_framework' and 'accounts' to the INSTALLED_APPS in settings.py.
# Step 2: Configure User Authentication
## User Model and Authentication:
Create a custom user model that extends Django’s AbstractUser, adding fields such as bio, profile_picture, and followers (a ManyToMany field referencing itself, symmetrical=False).
Set up Django REST Framework’s token authentication by adding 'rest_framework.authtoken' to your installed apps and running migrations to create the token model.
Implement views and serializers in the accounts app for user registration, login, and token retrieval.
# Step 3: Define URL Patterns
## Routing Configuration:
Configure URL patterns in accounts/urls.py to include routes for registration (/register), login (/login), and user profile management (/profile).
Ensure that registration and login endpoints return a token upon successful operations.
# Step 4: Testing and Initial Launch
## Server Testing:
Start the Django development server to ensure the initial setup is configured correctly: bash python manage.py runserver
Use tools like Postman to test user registration and login functionalities, verifying that tokens are generated and returned correctly.
## Deliverables:
Project Setup Files: Include all configuration files, initial migrations, and the Django project structure.
Code Files: Include models, views, and serializers for the user authentication system in the accounts app.
Documentation: Provide a README file detailing the setup process, how to register and authenticate users, and a brief overview of the user model.
Repo:

- GitHub repository: Alx_DjangoLearnLab
- Directory: social_media_api