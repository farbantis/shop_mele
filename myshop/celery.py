import os
from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myshop.settings')

# You create an instance of the application with app = Celery('myshop').
app = Celery('myshop')

# You load any custom configuration from your project settings using the
# config_from_object() method
app.config_from_object('django.conf:settings', namespace='CELERY')

# Finally, you tell Celery to auto-discover asynchronous tasks for your
# applications. Celery will look for a tasks.py file in each application
# directory of applications
app.autodiscover_tasks()
