from django.contrib import admin
from django.urls import path,include
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('meeting/', views.meeting, name='meeting'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login_user, name='login'),
    path('events/create/', views.create_event, name='events'),
    path('newevent/', views.event_list, name='upcomingevent'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)