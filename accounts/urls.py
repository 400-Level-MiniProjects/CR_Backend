from django.urls import path
from .views import *

app_name = 'accoounts'

urlpatterns = [
    path('register/', RegisterUser.as_view(), name='register')
]