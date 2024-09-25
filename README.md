# Django Ninja Docker Project

This project demonstrates how to set up a Django application with Django Ninja for API development, containerized using Docker. It serves as a simple task management API to showcase the integration of these technologies.

## Project Overview

We've created a basic Django project with the following key components:
- Django as the web framework
- Django Ninja for building APIs
- Docker for containerization
- Uvicorn as the ASGI server

## Step-by-Step Explanation

### 1. Project Setup

We started by creating a new Django project and a Django app:

```bash
django-admin startproject ninja_project .
python manage.py startapp ninja_tasks
```

**Why**: This sets up the basic structure for our Django application.

### 2. Django Ninja Integration

We integrated Django Ninja by adding it to `INSTALLED_APPS` in `settings.py` and creating an `api.py` file in our `ninja_tasks` app.

**Why**: Django Ninja allows us to easily create API endpoints with automatic documentation.

### 3. Model Creation

We defined a `NinjaTask` model in `models.py`:

```python
class NinjaTask(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
```

**Why**: This model represents the structure of our tasks in the database.

### 4. API Endpoints

We created CRUD (Create, Read, Update, Delete) endpoints in `api.py` using Django Ninja decorators.

**Why**: These endpoints allow us to interact with our `NinjaTask` model through the API.

### 5. Dockerization

We created a `Dockerfile` to containerize our application:

```dockerfile
FROM python:3.11-slim
# ... (rest of the Dockerfile content)
```

**Why**: Dockerization ensures our application runs consistently across different environments.

### 6. Environment Variables

We used environment variables for sensitive information and configuration:

```python
SECRET_KEY = os.getenv('SECRET_KEY')
DEBUG = os.getenv('DEBUG', 'False') == 'True'
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '*').split(',')
```

**Why**: This allows for flexible configuration without hardcoding sensitive data.

### 7. Running the Application

We use the following command to run our Dockerized application:

```bash
docker run -p 8000:8000 \
  -e SECRET_KEY="django-insecure-yxsv((49lxjfk+tp1=3zb)=+w%xgw&2a_0)&&z" \
  -e DEBUG=True \
  -e ALLOWED_HOSTS="localhost,127.0.0.1,0.0.0.0" \
  django-ninja-app
```

**Why**: This command:
- Maps port 8000 of the container to port 8000 on the host
- Sets necessary environment variables
- Specifies the Docker image to run

## Key Learning Points

1. **Django Project Structure**: Understanding how Django organizes projects and apps.
2. **API Development with Django Ninja**: Learning to create efficient API endpoints with automatic documentation.
3. **Dockerization**: Grasping the basics of containerizing a Django application.
4. **Environment Variables**: Managing application configuration securely.
5. **ASGI Server**: Using Uvicorn as an ASGI server for improved performance.

## Running the Project

1. Build the Docker image:
   ```bash
   docker build -t django-ninja-app .
   ```

2. Run the Docker container:
   ```bash
   docker run -p 8000:8000 \
     -e SECRET_KEY="your-secret-key" \
     -e DEBUG=True \
     -e ALLOWED_HOSTS="localhost,127.0.0.1,0.0.0.0" \
     django-ninja-app
   ```

3. Access the API documentation at `http://localhost:8000/api/docs`

## Conclusion

This project serves as a basic template for developing Django applications with API capabilities using Django Ninja, all containerized with Docker. It demonstrates best practices for structuring a Django project, creating API endpoints, and preparing the application for deployment in a containerized environment.
