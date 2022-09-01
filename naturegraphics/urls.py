from django.urls import path

from . import views

app_name = 'naturegraphics'
urlpatterns = [
    path('', views.IndexView, name='index'),
    path('contact', views.ContactView, name='contact')
    
]