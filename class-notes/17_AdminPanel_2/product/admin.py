from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import *

# * #########################
# *  CATEGORY
# * #########################
admin.site.register(Category)


# * #########################
# *  PRODUCT
# * #########################
class ReviewInline(admin.TabularInline):
    model = Review  #! ForeignKey modul name
    extra = 1  #! Yeni yorum ekleme alani
    classes = ["collapse"]


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
    # Resim gösterme read_only olarak çağır:
    readonly_fields = ["view_image"]
    # Form liste görüntüleme:
    fields = (
        ("name", "is_in_stock"),
        ("image", "view_image"),
        ("slug"),
        ("categories"),
        ("description"),
    )
    # filter_vertical = ["categories"]
    filter_horizontal = ["categories"]
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
    inlines = [ReviewInline]

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

    added_days_ago.short_description = "Days"
    list_display += ("added_days_ago",)

    # Kaçtane yorum var:
    def how_many_reviews(self, object):
        count = object.reviews.count()
        return count

    how_many_reviews.short_description = "Reviews"
    list_display += ("how_many_reviews",)

    # Listede küçük resim göster:
    def view_image_in_list(self, obj):
        from django.utils.safestring import mark_safe

        if obj.image:
            return mark_safe(
                f'<img src={obj.image.url} style="height:30px; width:30px;"></img>')
        return "-*-"

    view_image_in_list.short_description = "Image"
    list_display = ("view_image_in_list",) + list_display


admin.site.register(Product, ProductAdmin)


# * #########################
# *  REVIEW
# * #########################
class ReviewAdmin(ModelAdmin):
    list_display = ("__str__", "created_date")
    raw_id_fields = ("product",)


admin.site.register(Review, ReviewAdmin)
