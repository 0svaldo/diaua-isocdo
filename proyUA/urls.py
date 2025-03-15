
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static

admin.site.empty_value_display = '(nulo)'
admin.site.site_header = 'ISOC-DO #UADAY'
admin.site.site_title = 'ISOC-DO #UADAY - Módulo Administrativo'
admin.site.site_url = 'http://localhost:8000/admin'
admin.site.index_title = 'ISOC-DO #UADAY - Módulo Administrativo'
admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('appUA.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)