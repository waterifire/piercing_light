from django.urls import path

from .views import home, detail, word

# urlpatterns below

urlpatterns = [
        path('', home, name='mp_home'),
        path('detail/<str:pk>/', detail, name='mp_detail'),
        path('word', word, name='mp_word'),
        ]
