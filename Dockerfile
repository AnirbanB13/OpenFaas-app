FROM python:3.9-slim as base

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libjpeg-dev \
    zlib1g-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create upload directory for Flask
RUN mkdir -p /app/backend/uploads

# Set up Django static files
RUN cd frontend && python manage.py collectstatic --noinput

# Expose ports for Django and Flask
EXPOSE 8000 5000

# Create entrypoint script
RUN echo '#!/bin/bash\n\
cd /app/backend && python app.py & \n\
cd /app/frontend && gunicorn frontend.wsgi:application --bind 0.0.0.0:8000\n\
wait' > /app/entrypoint.sh && chmod +x /app/entrypoint.sh

# Set the entrypoint
ENTRYPOINT ["/app/entrypoint.sh"]