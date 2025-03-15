
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from .views import contact_view, index, success_view

urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact_view, name='contact'),
    path('success/', success_view, name='success'),  # Ruta de confirmación
]   