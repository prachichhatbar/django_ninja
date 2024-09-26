# Django Ninja Docker Project

## Project Overview

This project demonstrates a modern Django application setup, incorporating:
- Django web framework
- Django Ninja for API development
- Docker for containerization
- Uvicorn as an ASGI server

The application is a simple task management API, showcasing CRUD operations and API documentation.

## Project Structure

```
django_ninja/
├── ninja_project/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── ninja_tasks/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── api.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── static/
├── .dockerignore
├── .gitignore
├── .env
├── .env.example
├── Dockerfile
├── docker-compose.yml
├── manage.py
└── requirements.txt
```

## Setup and Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/django-ninja-docker.git
   cd django-ninja-docker
   ```

2. Create a `.env` file in the project root and add the following content:
   ```
   DJANGO_SECRET_KEY=your_secret_key_here
   DJANGO_DEBUG=True
   DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1,0.0.0.0
   ```
   Replace `your_secret_key_here` with a secure secret key.

3. Build and start the Docker containers:
   ```
   docker-compose up --build
   ```

4. Access the API documentation at `http://localhost:8000/api/docs`

## Docker Usage

The project uses Docker and Docker Compose for easy setup and deployment.

- To start the project:
  ```
  docker-compose up
  ```

- To rebuild the Docker image after making changes:
  ```
  docker-compose up --build
  ```

- To stop the project:
  ```
  docker-compose down
  ```

- To view logs:
  ```
  docker-compose logs
  ```

## Development Workflow

1. Make changes to your Django code.
2. If you've made changes to the Python dependencies, update `requirements.txt`.
3. Rebuild and restart the Docker containers:
   ```
   docker-compose up --build
   ```
4. Access your application at `http://localhost:8000/api/docs` to see the changes.

## Key Components

### Django Project (ninja_project)

The main Django project configuration.

- `settings.py`: Contains project settings, including database configuration, installed apps, and middleware.
- `urls.py`: Defines the URL routing for the project.

### Django App (ninja_tasks)

The main application containing the API logic.

- `models.py`: Defines the `NinjaTask` model.
- `api.py`: Contains the API endpoints using Django Ninja.

### Dockerfile

The Dockerfile sets up the Python environment, installs dependencies, and configures the Django application for running with Uvicorn.

### docker-compose.yml

Defines the services, networks, and volumes for the Docker setup. It specifies how to build and run the Django application container.

## Environment Variables

The project uses the following environment variables:

- `DJANGO_SECRET_KEY`: The secret key for Django.
- `DJANGO_DEBUG`: Set to `True` for development, `False` for production.
- `DJANGO_ALLOWED_HOSTS`: Comma-separated list of allowed hosts.

These are defined in the `.env` file and passed to the Docker container.

## API Endpoints

- `GET /api/tasks`: List all tasks
- `POST /api/tasks`: Create a new task
- `GET /api/tasks/{task_id}`: Retrieve a specific task
- `PUT /api/tasks/{task_id}`: Update a specific task
- `DELETE /api/tasks/{task_id}`: Delete a specific task

## Testing

To run tests:

```
docker-compose run web python manage.py test
```

## Deployment

This project is set up to be easily deployable to any Docker-compatible hosting service. Ensure that you set the appropriate environment variables for production use.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.