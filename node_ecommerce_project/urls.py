# ecommerce_project/urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('store/', include('store.urls')),
    path('accounts/', include('django.contrib.auth.urls')),  # Include authentication URLs

]
