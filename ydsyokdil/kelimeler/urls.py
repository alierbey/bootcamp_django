from django.urls import path
from . import views


urlpatterns = [
    path('', views.kelime_list, name="kelimeler"),
    path('<str:kelime_name>', views.kelime_detail, name="kelime_detail"),
    path('kategori/<str:kategori_name>',
         views.kategori_detail, name="kategori_detail")
]
