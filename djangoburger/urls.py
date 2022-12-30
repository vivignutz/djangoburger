from django.contrib import admin
from . import views
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from .views import (home,
                    products,
                    contact,
                    login,
                    register
)

urlpatterns = [
    path('djangoburger/', views.home, name='home'),
    path('product/', views.details_product, name='product')
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)