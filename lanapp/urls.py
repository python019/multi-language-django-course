from django.urls import path
from .views import home

app_name = 'lanapp'

urlpatterns = [
    path('', home),
]
