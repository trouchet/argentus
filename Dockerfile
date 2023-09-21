# Use an official Python runtime as a parent image
FROM python:3.8-slim-buster

# Set environment variables for Python (recommended)
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONFAULTHANDLER=1
ENV PYTHONHASHSEED=random
ENV PIP_NO_CACHE_DIR=off
ENV PIP_DISABLE_PIP_VERSION_CHECK=on

# Create and set the working directory
WORKDIR /app

# Install system dependencies (if needed)
RUN pip install poetry

# Copy only the project files needed initially
COPY . /app/
COPY scripts/deploy-utils.sh /app/

# Install project dependencies using Poetry within a virtual environment
RUN poetry config virtualenvs.create false && \
    poetry install --only main --no-interaction --no-ansi

# Set executable permissions for the script
RUN chmod +x /app/deploy-utils.sh

# Start the Django development server within the virtual environment
# Run database migrations and collect static files before starting the Django app
CMD ["./deploy-utils.sh"]
