from django.urls import path

from . import views
from news import views

app_name = 'news'

urlpatterns = [
    path('', views.index, name='index'),
    path('headline/', views.headline, name='headline'),
]