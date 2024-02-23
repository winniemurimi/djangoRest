from django.urls import path
from .views import send_message
from . import views


urlpatterns = [
    path('', views.getData),
    path('add/', views.addItem),
    path('send_message/', send_message, name='send_message')
]
