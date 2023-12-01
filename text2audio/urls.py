from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name="index"),   
    path("text2audio/", text2audio, name="text2audio"),
    
]