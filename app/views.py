from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from .models import Event


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

@login_required
def create_event(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        pdf = request.FILES.get('pdf')

        Event.objects.create(
            title=title,
            description=description,
            pdf=pdf
        )

        return redirect('events')  # your event list page

    return render(request, 'app/event.html')

def event_list(request):
    events = Event.objects.order_by('title')  
    return render(request, 'app/upcomingevent.html', {'events': events})