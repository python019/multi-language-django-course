from django.shortcuts import render

# Create your views here.
def home(request, slug):
    return render(request, 'lanapp/index.html')