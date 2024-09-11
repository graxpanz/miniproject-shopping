from django.contrib import admin
from supproduct.models import Suppro

class supproducts(admin.ModelAdmin):
    list_display=["name","price","stock","isTrending"]
    list_editable=["price","stock","isTrending"]
    list_per_page=5
    search_fields=["name"]
    list_filter=["isTrending"]

# Register your models here.
admin.site.register(Suppro,supproducts)