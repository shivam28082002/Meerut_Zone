"""
URL configuration for meerut_zone_web project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('login/', login_view, name='login'),
    path('signup/', signup, name='signup'),
    path('hospital_data/', hospital_data, name='hospital_data'),
    path('eduction/', eduction, name='eduction'),
    path('park/', park, name='park'),
    path('shopping/', shopping, name='shopping'),
    path('cafes/', cafes, name='cafes'),
    path('bank/', bank, name='bank'),
    path('contact_us/', contact_us, name='contact_us'),
    path('logout_view/', logout_view , name='logout_view'),
    path('check_email/', check_email , name='check_email'),
    path('profile/', profile , name='profile'),
    path('data_hospital/', data_hospital, name='data_hospital'),
    path('data_eduction/', data_eduction, name='data_eduction'),
    path('data_cafes/', data_cafes, name='data_cafes'),
    path('data_bank/', data_bank, name='data_bank'),
    path('data_park/', data_park, name='data_park'),
    path('data_shopping/', data_shopping, name='data_shopping'),
    path('change_password_view/', change_password_view, name='change_password_view'),
    path('forget_password_view/', forget_password_view, name='forget_password_view'),
    path('reset_password/<uidb64>/<token>/', reset_password_view, name='reset_password'),
    path('chat_bot/', chatbot_view, name='chat_bot'),
    path('review/', review, name='review')
    
] 
