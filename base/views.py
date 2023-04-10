from django.shortcuts import render
from .models import Client, Contact

# Create your views here.


def home_page(request):
    clients = Client.objects.all()
    return render(request, 'index.html', {'clients': clients})


def more_services(request):
    return render(request, 'more_services.html')
