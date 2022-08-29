from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import SignupForm, JournalForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Profile
from django.core.mail import send_mail
import datetime
from django.utils import timezone
import schedule
import time
from .models import Journals
from django.conf import settings
# Create your views here.

def home(request):
    form = JournalForm()
    ctx = {'form' : form}
    if request.method == "POST":
        form = JournalForm(request.POST)
        user = request.user
        if form.is_valid():
            page = 'journal'
            ctx ={'page': page}
            body = request.POST.get('body')
            profile = Profile.objects.get(owner = user)
            journal = Journals.objects.create(body = body, posted_by = profile)
            journal.save()
            send_journals(request)
            return render(request, 'app/success.html', ctx)
        else:
            print("Error Posting Journal")
    return render(request, 'app/index.html', ctx)

def signup(request):
    form = SignupForm()
    page = 'signup'

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            profile = Profile.objects.create(owner=user)
            profile.save()
          
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Signup Unsuccessful. Please check you filled the form correctly")

    ctx = {'page': page, 'form': form}
    return render(request, 'app/auth.html', ctx)

def login_user(request):

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User doesnt exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request,'Logged in!')
            return redirect('home')
        else:
            messages.error(request, 'username or password doesnt exist')
    ctx = {}
    return render(request, 'app/auth.html', ctx)

def logout_user(request):
    logout(request)
    return redirect('home')

def send_journals(request):
    journals = Journals.objects.all() 

    for journal in journals:
        emails = journal.posted_by.owner.email
   
        messages = journal.body
        subject  = "New Journal Entry."
        sender = settings.EMAIL_HOST_USER
        send_mail(subject, messages, sender, [emails])

    return redirect("home")



