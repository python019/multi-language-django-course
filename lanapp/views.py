from django.shortcuts import render, get_object_or_404
from .models import Malumot
# Create your views here.
def home(request):
    return render(request, 'lanapp/home.html')

def malumot(request, slug):
    malumot = get_object_or_404(Malumot, slug=slug)
    context = { 
        'malumot': malumot
    }
    return render(request, 'lanapp/index.html', context)