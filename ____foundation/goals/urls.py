from django.urls import path

from .views import goals_home, goals_add

# urlpatterns below

urlpatterns = [
    path('home/', goals_home, name='goals_home'),
    path('add/', goals_add, name='goals_add'),
]
