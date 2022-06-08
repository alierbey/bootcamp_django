from django.shortcuts import render

def kelime_list(request):
    return render(request, "kelimeler.html")
