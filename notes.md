




##### Order of migrations execution. Use it after changing your model(s) in models.py
python manage.py ...->
- makemigrations polls
- sqlmigrate polls 0001
- migrate
