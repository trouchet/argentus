#!/bin/bash

# Function to display usage information
usage() {
    exit 1
}

# Check if the port argument is provided
if [ $# -ne 1 ]; then
    usage
fi

# Collect static files
poetry run uvicorn main:app --reload
