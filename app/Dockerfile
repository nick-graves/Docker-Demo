# Use an official Python runtime as a base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the local project files to the container
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Expose the application port (Flask runs on 5000)
EXPOSE 5000

# Define the command to run the app
CMD ["python", "app.py"]