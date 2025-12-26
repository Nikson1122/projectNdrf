from django.contrib import admin
from django.urls import path,include
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('meeting/', views.meeting, name='meeting'),
    # path('contact/', views.contact, name='contact'),
    path('login/', views.login_user, name='login'),
    path('events/create/', views.create_event, name='events'),
    path('newevent/', views.event_list, name='upcomingevent'),
    path('logout/', views.logout_user, name='logout'),
    path('addproduct/', views.add_product, name='addproduct'),
    path('ourstore/', views.our_store, name='ourstore'),
    path('buy/<int:product_id>/', views.buy_product, name='buy_product'),
    path('orders/', views.order_list, name='order_list'),
    path('contact', views.contact_view, name='contact'),
    path('contact/messages/', views.contact_messages_view, name='contact_messages'),
    path('blog/', views.blog, name='blog'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)