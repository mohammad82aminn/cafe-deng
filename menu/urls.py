from django.urls import path

from . import views

app_name = 'menu'

urlpatterns = [
    path('', views.menu_home, name='home'),
    path('drinks/', views.drinks, name='drinks'),
    path('desserts/', views.desserts, name='desserts'),
]