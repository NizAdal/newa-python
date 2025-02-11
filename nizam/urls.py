"""
URL configuration for new project.

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
from django.urls import path, include
from nizam import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.contrib.auth import views as auth_view
urlpatterns = [
    path('',views.home, name='home'),
    path('posts/', views.posts, name ='posts'),
    path('blogpost/<str:slug>',views.blogpost, name ='blog'),
    path('contact/',views.contact, name='contact'),
    path('membership/',views.membership, name='membership'),
    path('membersdetail/',views.membersdetail, name='membersdetail'),
    path('notes/',views.notes, name='notes'),
    path('getnotes/',views.getnotes, name='getnotes'),

    path('search/',views.search, name='search'),
    path('filenotes/<int:pk>',views.filenotes, name='filenotes'),
    path('startsurvey/',views.startsurvey, name='startsurvey'),
    path('survey',views.survey, name='survey'),
    path('sendmail/', views.send_mail_to_all, name='sendmail'),
    path('schedulemail/', views.schedule_mail, name='schedulemail'),
    

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
