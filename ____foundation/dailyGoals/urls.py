from django.urls import path

from .views import dg_home, dg_add

# Urlpatterns below

urlpatterns = [
    path('', dg_home, name='dg_home'),
    path('add/', dg_add, name='dg_add'),
]
