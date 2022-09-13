#!bin/bash

echo "Starting database migration!!"
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata ./initialData.json
echo "Database migration complete!!"
