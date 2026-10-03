# pages/views.py
from django.shortcuts import render
from django.views import View


def home(request):
    context = {
        'cafe_name': 'Cafe Deng',
        'slogan': 'Best coffee in town, served with a smile.',
        'opening_hours': 'Every day, 8:00 AM to 11:00 PM',
    }
    return render(request, 'home.html', context)

class AboutView(View):
    def get(self, request):
        context = {
            'cafe_name': 'Cafe Deng',
            'year': 2020,
            'team_size': 6,
            'address': '12 Valiasr St, Tehran',
        }
        return render(request, 'pages/about.html', context)
        
