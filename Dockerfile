# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy requirements.txt first to leverage Docker cache
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files
COPY . .

# Set the host for Flask to listen on all interfaces
ENV FLASK_RUN_HOST=0.0.0.0

# Expose port 8080 to the outside world
EXPOSE 8080

# Run the Flask application
CMD ["flask", "run"]
