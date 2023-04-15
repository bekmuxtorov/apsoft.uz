from django.shortcuts import render
from .models import Client, Contact
from .forms import ContactForm
import os
import requests

# Create your views here.


def send_telegram(message_data: dict):
    BOT_TOKEN = os.environ.get('BOT_TOKEN')
    ADMINS = os.environ.get('ADMINS').split(',')
    url = "https://api.telegram.org/bot" + BOT_TOKEN + "/sendMessage"
    message = "Ismi: " + message_data.get('full_name') + "\nEmail: " + \
        message_data.get('email') + "\nMavzu: " + \
        message_data.get('subject') + "\n\nXabar: " + \
        message_data.get('message')
    for admin in ADMINS:
        try:
            requests.post(url, {'chat_id': admin, 'text': message})
        except Exception:
            pass

def home_page(request):
    msg = False
    print(request)
    if request.method == "POST":
        print(request)
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            send_telegram(request.POST)
            msg = True
    clients = Client.objects.all()
    return render(request, 'index.html', {'clients': clients, 'msg': msg})


def more_services(request):
    return render(request, 'more_services.html')


def more_clients(request):
    clients = Client.objects.all()
    return render(request, 'more_clients.html', {'clients': clients})
