from django.contrib import admin
from . models import Kategori, Kelime

# Register your models here.


@admin.register(Kelime)
class KelimeAdmin(admin.ModelAdmin):
    list_display = ('name', 'available')
    list_filter = ('available',)
    search_fields = ('name', 'description')


@admin.register(Kategori)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
