# Start with official Python image
FROM python:3.9

# Set the working directory inside the container where all other commands will be run
WORKDIR /app

# Copy the project files to the container
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Expose the application port 
EXPOSE 5000

# Define the command to run the app
CMD ["python", "app.py"]