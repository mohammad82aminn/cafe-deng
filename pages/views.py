# pages/views.py
from django.shortcuts import render


def home(request):
    context = {
        'cafe_name': 'Cafe Deng',
        'slogan': 'Best coffee in town, served with a smile.',
        'opening_hours': 'Every day, 8:00 AM to 11:00 PM',
    }
    return render(request, 'home.html', context)