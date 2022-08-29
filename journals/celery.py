import os
from django.conf import settings
from celery import Celery
from celery.schedules import crontab
# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'journals.settings')

app = Celery('journals')
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

app._autodiscover_tasks(settings.INSTALLED_APPS, related_name='tasks')

app.conf.beat_schedule = {
    'add-every-2-hour' : {
        "task" : 'send_journal',
        'schedule' : crontab(minute='*/1')
    }
}

@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')