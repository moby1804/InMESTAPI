from django.urls import path
from .views import *

urlpatterns = [
    
    path('say hello/', say_hello, name ='hello page'),
]
