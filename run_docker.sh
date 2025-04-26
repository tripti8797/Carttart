#!/bin/bash

# Build the Docker images
docker-compose build

# Run the containers
docker-compose up -d

# Run database migrations (on the migrate service)
docker-compose run migrate python manage.py migrate

# Create a superuser (optional but recommended)
docker-compose run migrate python manage.py createsuperuser

# Collect static files (if applicable)
docker-compose run migrate python manage.py collectstatic --noinput
