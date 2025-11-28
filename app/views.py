from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'app/base.html')

def about(request):
    return render(request, 'app/about.html')

def meeting(request):
    return render(request, 'app/meeting.html')