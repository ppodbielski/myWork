import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'michal_site.settings')

app = Celery('michal_site')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
#app.conf.task_default_queue = 'kolejka'


#app.autodiscover_tasks([a for a in settings.INSTALLED_APPS])
