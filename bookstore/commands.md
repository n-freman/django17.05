python manage.py dumpdata > data.json
python manage.py flush
python manage.py loaddata data.json
python manage.py shell