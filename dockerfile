# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Create and set the working directory
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# At the bottom, after COPY and pip install
# RUN python manage.py collectstatic --noinput


# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app/

# Expose port 8000 for the Django app
EXPOSE 8000

# Command to run the application (e.g., start Django development server)
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

CMD ["sh", "run_docker.sh"]
