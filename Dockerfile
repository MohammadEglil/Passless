# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Copy the requirements.txt file and install dependencies
COPY requirements.txt . 

RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire app to the container's working directory
COPY ./backend .

# Expose the port the app runs on
EXPOSE 80

# Command to run Uvicorn directly
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80", "--workers", "4"]
