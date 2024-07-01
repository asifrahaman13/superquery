# Use the official Python image from the Docker Hub
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt ./

# Install any needed packages specified in requirements.txt
RUN apt-get update && \
    apt-get install -y redis-server && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application into the container
COPY . .

# Copy the Redis configuration file
COPY redis.conf /usr/local/etc/redis/redis.conf

# Expose the port that the application will run on
EXPOSE 8000

# Expose the port Redis runs on
EXPOSE 6379

# Start both Redis and the FastAPI app
CMD redis-server /usr/local/etc/redis/redis.conf --daemonize yes && uvicorn src.main:app --host 0.0.0.0 --reload