# Use the official Python base image
FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files to the working directory
COPY . .

# Run any additional commands to prepare your app (e.g., migrations, collectstatic)
# Example:
# RUN python manage.py migrate
# RUN python manage.py collectstatic --noinput

# Expose the port that your Django app will run on
EXPOSE 8000

# Specify the command to run your Django app
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
