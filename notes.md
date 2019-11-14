https://docs.djangoproject.com/en/2.2/intro/tutorial05/


##### Order of migrations execution. Use it after changing your model(s) in models.py
python manage.py ___->
- makemigrations polls
- sqlmigrate polls 0001
- migrate

---

```
from django.test.utils import setup_test_environment
setup_test_environment()
from django.test import Client
client = Client()
from django.urls import reverse
response = client.get(reverse('polls:index'))
response.status_code
response.content
response.context['latest_question_list']
```