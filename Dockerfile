# Use the official Alpine Linux base image
FROM python:3.11

# Set the working directory inside the container
WORKDIR /app

# Copy all files from the host working directory to the container working directory
COPY . .

# Start the shell
RUN apt-get update && apt-get install -y redis-server

# Run Redis in the background and then start the Flask application
CMD ["sh", "-c", "redis-server"]