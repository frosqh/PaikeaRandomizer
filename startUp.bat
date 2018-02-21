call virtualenv\Scripts\activate
python manage.py makemigrations randomizer
python manage.py sqlmigrate randomizer 0001 &
python manage.py migrate
python manage.py runserver localhost:8888 &