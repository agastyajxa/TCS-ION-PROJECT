#!/bin/bash

# Define the container name
CONTAINER_NAME="weather_app-weather-app-1"

# Check if the container is running
if [ "$(docker ps -q -f name=$CONTAINER_NAME)" ]; then
    echo "Container '$CONTAINER_NAME' is already running. Not running 'docker-compose up -d'."
else
    echo "Container '$CONTAINER_NAME' is not running. Running 'docker-compose up -d'."
#    docker-compose up -d
    cd /home/ubuntu/jenkins-pipeline/src/main/python/weather_app && docker-compose up -d
fi
