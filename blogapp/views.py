from django.shortcuts import render
from django.http import HttpResponse

news = [
    {
        'title': 'Наша первая запись',
        'text': 'our ПРосто большой текст для 1й записи',
        'date': '29.12.2019',
        'author': 'Георгий'
    },
    {
        'title': 'Наша первая запись',
        'text': 'our ПРосто большой текст для 2й записи',
        'date': '28.12.2019',

    },
]


def home(request):
    data = {
        'news': news,
        'title': 'Main blog page',
    }
    return render(request, 'blogapp/home.html', data)


def contacts(request):
    return render(request, 'blogapp/contacts.html', {'title': 'page about us'})
