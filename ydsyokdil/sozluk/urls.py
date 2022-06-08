from django.urls import path
from . import views

urlpatterns = [
        path('',views.sozluk, name = "sozluk")
]