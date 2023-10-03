from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import *


# Create your views here.
def index(request):
    return render(request, 'home.html')


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def notes(request):
    return render(request, 'notes.html')

from .models import*
def contact(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        contact_user = Contact(full_name=full_name, email=email, message=message)
        contact_user.save()
    return render(request, 'contact.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User(username=username, first_name=first_name, last_name=last_name, email=email, password=password)
        user.save()
        return redirect('login')
    return render(request, 'signup.html')

class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'signup.html'
    success_url = '/'


# class LogInView(CreateView):
#     form_class = AuthenticationForm
#     template_name = 'login.html'
#     success_url = '/'


def login(request):
    if request.method =="POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(user)
                return redirect('homepage')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form':form})