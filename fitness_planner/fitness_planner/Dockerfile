# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /fitness_tracker

# Copy the current directory contents into the container at /app
COPY . /fitness_tracker

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define the command to run your application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

ENV REDIS_REMOTE_PORT=6379 \
    REDIS_REMOTE_HOST=host.docker.internal \
    POSTGRES_REMOTE_PORT=5432 \
    POSTGRES_REMOTE_HOST=host.docker.internal \
    RELEASE_VERSION=${VERSION} \
    OPENSSL_CONF=/home/integration-proxy/openssl.cnf