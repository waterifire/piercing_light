from django.urls import path

from .views import goals_home, goals_add, goals_edit

# urlpatterns below

urlpatterns = [
    path('home/', goals_home, name='goals_home'),
    path('add/', goals_add, name='goals_add'),
    path('edit/<str:pk>/', goals_edit, name='goals_edit'),
]
