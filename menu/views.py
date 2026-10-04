from django.shortcuts import render

# Create your views here.
def menu_home(request):
    return render(request, 'menu/home.html')

def drinks(request):
    context = {
        'category': 'Drinks',
        'icon': '☕',
        'description': 'Hot and cold drinks, made fresh for you.',
        'best_seller': 'Caramel Latte',
        'price': 85000,
    }
    return render(request, 'menu/category.html', context)


def desserts(request):
    context = {
        'category': 'Desserts',
        'icon': '🍰',
        'description': 'Homemade cakes and sweets, baked every morning.',
        'best_seller': 'New York Cheesecake',
        'price': 120000,
    }
    return render(request, 'menu/category.html', context)