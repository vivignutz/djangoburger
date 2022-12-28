from django.contrib import admin
from . import views
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('djangoburger/', views.home, name='home'),
    path('product/', views.details_product, name='product')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

