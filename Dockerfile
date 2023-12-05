# syntax=docker/dockerfile:1

# Use an official Python runtime as the base image
FROM python:3.11-slim-buster

# Set the working directory in the container to /app
WORKDIR /app

COPY requirements.txt requirements.txt

# Install Flask and other dependencies

RUN pip3 install -r requirements.txt

# Copy the current directory (our Flask app) into the container at /app
COPY . .

# Run the command to start the Flask app

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]