from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('realestate.urls')),
    path('contacts/', include('contacts.urls')), 
    path('logmein/', include('logmein.urls')),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
