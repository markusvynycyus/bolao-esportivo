from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path('admin/', admin.site.urls),
    path('aposta/', include('aposta.urls',namespace='aposta'))
    path('', include('bets.urls', namespace='bets')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)