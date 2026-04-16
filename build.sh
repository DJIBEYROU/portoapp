#!/usr/bin/env bash
# Build script for Render

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Create static directory if it doesn't exist
mkdir -p staticfiles

# Collect static files
python manage.py collectstatic --noinput
