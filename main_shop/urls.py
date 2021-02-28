from django.urls import path
from . import views


urlpatterns = [
    path('', views.register, name='guitar_in_stock'),
    path('guitar_ex', views.GuitarEx, name='guitar_ex')
]