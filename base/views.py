from django.shortcuts import render
from .models import Client, Contact
from .forms import ContactForm

# Create your views here.


def home_page(request):
    msg = False
    print(request)
    if request.method == "POST":
        print(request)
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            msg = True
    clients = Client.objects.all()
    return render(request, 'index.html', {'clients': clients, 'msg': msg})


def more_services(request):
    if request.method == "POST":
        print('alo asdfaf')
    return render(request, 'more_services.html')


def more_clients(request):
    clients = Client.objects.all()
    return render(request, 'more_clients.html', {'clients': clients})
