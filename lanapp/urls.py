from django.urls import path
from .views import home, malumot

app_name = 'lanapp'

urlpatterns = [
    path('', home,),
    path('<slug:slug>/', malumot, name="malumot"),
]
