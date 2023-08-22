from django.contrib import admin 
from django.urls import path,include
 
# Three modules for swagger:
from rest_framework import permissions 
from drf_yasg.views import get_schema_view 
from drf_yasg import openapi 
 
 
schema_view = get_schema_view( 
    openapi.Info( 
        title="Rent a Car", 
        default_version="v1", 
        description="Rent a Car API project provides Rent a Car management", 
        terms_of_service="#", 
        contact=openapi.Contact(email="16fay61@gmail.com"),  # Change e-mail on this line! 
        license=openapi.License(name="BSD License"), 
    ), 
    public=True, 
    permission_classes=[permissions.AllowAny], 
) 
 
urlpatterns = [ 
    path("admin/", admin.site.urls), 
 
    # Url paths for swagger: 
    path("swagger(<format>\.json|\.yaml)", schema_view.without_ui(cache_timeout=0), name="schema-json"), 
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"), 
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    #for debug toolabar
    path('__debug__/', include('debug_toolbar.urls')),
    
    #my urls
    path('users/', include('users.urls')),
    path('api/', include('rent_car.urls')),
]

# image kullandığım için

from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# canlı da seç beğen https://django-storages.readthedocs.io/en/latest/