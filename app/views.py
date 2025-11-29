from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


# Create your views here.

def home(request):
    return render(request, 'app/base.html')

def about(request):
    return render(request, 'app/about.html')

def meeting(request):
    return render(request, 'app/meeting.html')

def contact(request):
    return render(request, 'app/contact.html')

def login_user(request):
    if request.method == 'POST':
         username = request.POST.get('username')
         password = request.POST.get('password')

         user = authenticate(request, username=username, password=password)

         if user is not None:
             login(request, user)
             return redirect('events')
         else:
                return render(request, 'app/login.html', {'error': 'Invalid username or password'})
         
    return render(request, 'app/login.html')