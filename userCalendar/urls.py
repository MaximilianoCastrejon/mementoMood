from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from . import views

app_name = 'userCalendar'

urlpatterns = [
	path('', views.home_calendar, name="home"),
]
