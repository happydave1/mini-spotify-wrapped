from django.urls import path
from api_section.views import main

urlpatterns = [
    path('', main)
]