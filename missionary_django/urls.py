from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/rainbow/', include('rainbow.urls')),
    path('api/v1/blog/', include('blog.urls')),
    path('api/v1/resources/', include('resources.urls'))
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
