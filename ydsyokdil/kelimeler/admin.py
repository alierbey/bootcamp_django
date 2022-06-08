from django.contrib import admin
from . models import Kelime

# Register your models here.

@admin.register(Kelime)
class KelimeAdmin(admin.ModelAdmin):
    list_display = ('name', 'available')
    list_filter = ('available',)
    search_fields =  ('name', 'description')
