from django.urls import path
from . import views


urlpatterns = [
    path('', views.kelime_list, name="kelimeler"),
]
