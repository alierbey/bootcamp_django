from django.shortcuts import render
from . models import Kelime, Kategori


def kelime_list(request):
    kelimeler = Kelime.objects.all()
    kategoriler = Kategori.objects.all()

    context = {
        'kelimeler': kelimeler,
        'kategoriler': kategoriler
    }

    return render(request, "kelimeler.html", context)


def kelime_detail(request, kelime_name):
    kelime = Kelime.objects.get(name=kelime_name)

    context = {
        'kelime': kelime
    }
    return render(request, "kelime.html", context)


def kategori_detail(request, kategori_name):

    kategori_id = Kategori.objects.get(slug=kategori_name)
    kelimeler = kategori_id.kelime_set.all()

    context = {
        'kelimeler': kelimeler
    }
    return render(request, "kelimeler.html", context)
