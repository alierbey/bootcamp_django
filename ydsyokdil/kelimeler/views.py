from django.shortcuts import render
# from . models import Kelime

# Create your views here.

def kelime_list(request):
    # kelimeler = Kelime.object.all()

    # context = {
    #     'kelimeler' : kelimeler
    # }


    return render(request, "kelimeler.html")
