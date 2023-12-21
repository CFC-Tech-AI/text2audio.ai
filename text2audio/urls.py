from django.urls import path
from .views import *

urlpatterns = [
      
    path("", text2audio, name="text2audio"),
    
]