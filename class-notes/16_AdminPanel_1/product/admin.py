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
    list_max_show_all = 200  #! Tumunu goster derken max gosterim sayisi
    date_hierarchy = "create_date"  #! Tarih field olmak zorunda
    prepopulated_fields = {
        "slug": ["name"]
    }  #! name i doldurunca otomatik slug olusturuyor
    # Form liste görüntüleme:
    fields = (
        ("name", "is_in_stock"),
        ("slug"),
        ("description"),
    )
    """
    #* Detayli form liste görüntüleme:
    fieldsets = (
        ('General Settings', {
            # "classes": ['wide'],
            "fields": (
                ('name', 'is_in_stock'),
                ('slug'),
            )
        }),
        ('Optional Settings', {
            "classes": ['collapse'],
            "fields": (
                ('description'),
            ),
            'description': "You can use this section for optionals settings"
        }),
    )
    """

    def set_stock_in(self, request, queryset):
        count = queryset.update(is_in_stock=True)
        self.message_user(request, f'{count} adet "Stokta Var" olarak işaretlendi.')

    def set_stock_out(self, request, queryset):
        count = queryset.update(is_in_stock=False)
        self.message_user(request, f'{count} adet "Stokta Yok" olarak işaretlendi.')

    actions = ("set_stock_in", "set_stock_out")
    set_stock_in.short_description = "İşaretli ürünleri stoğa ekle"
    set_stock_out.short_description = "İşaretli ürünleri stoktan çikar"

    def added_days_ago(self, object):
        from django.utils import timezone

        different = timezone.now() - object.create_date
        return different.days

    list_display += ("added_days_ago",)


admin.site.register(Product, ProductAdmin)


# * #########################
# *  PRODUCT
# * #########################
admin.site.register(Review)
