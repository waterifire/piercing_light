from django.urls import path

from .views import home

# urlpatterns below


urlpatterns = [
    path('', home, name='home')
]
