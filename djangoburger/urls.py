from django.contrib import admin
from . import views
from django.urls import path


urlpatterns = [
    path('djangoburger/', views.home, name='home'),
    path('product/', views.details_product, name='product')
]