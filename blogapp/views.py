from django.shortcuts import render
from .models import News

def home(request):
    data = {
        'news': News.objects.all(),
        'title': 'Main blog page',
    }
    return render(request, 'blogapp/home.html', data)


def contacts(request):
    return render(request, 'blogapp/contacts.html', {'title': 'page about us'})
