from journals.celery import app
import datetime
from django.core.mail import send_mail
from django.conf import settings


@app.task(name="send_journal")
def send_journal():
    try:
        from .models import Journals
        time_threshold = datetime.now() - datetime.timedelta(days=1)
        journals = Journals.objects.filter(date_posted__gte=time_threshold)
        for journal in journals:
            emails = journal.posted_by.owner.email
            subject = "New Journal Entry"
            email_from = settings.EMAIL_HOST_USER
            messages = journal.body

            send_mail(subject, messages, email_from, [emails])



    except Exception: 
        print(Exception)
