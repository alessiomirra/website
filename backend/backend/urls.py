from django.contrib import admin
from django.urls import path, include 
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('rest_framework.urls')), 
    path('api/', include("cars.api.urls")), 
    path('newsletter/', include('newsletter.urls')), 
]

if settings.DEBUG: 
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT, 
    )