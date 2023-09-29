# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Create and set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Copy the rest of the application code into the container
COPY . /app

# Expose port 5000 for Flask to run
EXPOSE 5000

# Define the command to run your Flask application
CMD ["python", "backend.py"]
