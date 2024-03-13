# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /fitness_planner

# Copy the current directory contents into the container at /app
COPY . /fitness_planner

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8000

ENV REDIS_REMOTE_PORT=6379 \
    REDIS_REMOTE_HOST=host.docker.internal \
    POSTGRES_REMOTE_PORT=5432 \
    POSTGRES_USERNAME=postgres \
    POSTGRES_PASSWORD=postgres \
    RELEASE_VERSION=${VERSION} \
    OPENSSL_CONF=/home/integration-proxy/openssl.cnf
    
# Define the command to run your application

CMD sh -c "python manage.py migrate && python manage.py management/commands/create_sample_dataset && python manage.py runserver 0.0.0.0:8000"

