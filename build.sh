#!/usr/bin/env bash
# Build script for Render
pip install -r requirements.txt
python manage.py migrate --noinput
python manage.py collectstatic --noinput
