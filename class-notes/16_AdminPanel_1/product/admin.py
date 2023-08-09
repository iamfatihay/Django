from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import *


# * #########################
# *  PRODUCT
# * #########################


class ProductAdmin(ModelAdmin):
    list_display = (
        "id",
        "name",
        "description",
        "is_in_stock",
        "create_date",
        "update_date",
    )  #! Tablo sutunlari
    list_editable = ["is_in_stock"]  #! Tablo uzerinde edit islemi yapabilme
    list_display_links = ["id", "name"]  #! Kayda gitmek icin linkleme
    list_filter = ["is_in_stock", "create_date", "update_date"]  #! filtreleme
    search_fields = ["id", "name"]  #! Searching
    search_help_text = "Arama yapmak icin burayi kullaniniz"
    ordering = ["id"]  #! "id" >> ASC   "-id" >> DESC
    list_per_page = 20  #! Sayfa basi product sayisi
    list_max_show_all = 200 #! Tumunu goster derken max gosterim sayisi
    date_hierarchy = "create_date"


admin.site.register(Product, ProductAdmin)


# * #########################
# *  PRODUCT
# * #########################
admin.site.register(Review)
