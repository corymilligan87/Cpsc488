"""These are the URL modules which are built outside of the ResReq application"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# These are the URL patterns which function outside of the ResReq application, but within the project.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalog/', include('catalog.urls')),
    path('', include('django.contrib.auth.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts', include('django.contrib.auth.urls')),
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
