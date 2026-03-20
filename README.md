# CineReserve

## About

The CineReserve API is a RESTful backend for managing cinema operations.

## Environment Variables

- Create a ```.env``` in the application root directory and fill with the necessary values.
- Use ```.env.example``` as reference.

## Running with Docker

### Requirements
- Docker + Docker Compose installed.

### Steps

1. Clone the repository:

    ```
    git clone https://github.com/alfredoherculano/cinereserve
    cd cinereserve
    ```

2. Start the services:

    ```docker compose up --build```

3. Run migrations (only on the first execution):

    ```docker compose exec django-web python manage.py migrate```

4. Access the app:

    ```http://127.0.0.1:8000/api```