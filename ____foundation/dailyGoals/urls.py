from django.urls import path

from .views import dg_home, dg_add, dn_add

# Urlpatterns below

urlpatterns = [
    path('', dg_home, name='dg_home'),
    path('add_daily_goal/', dg_add, name='dg_add'),
    path('add_note', dn_add, name='dn_add')
]
