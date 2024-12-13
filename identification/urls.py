from django.urls import path, include
# to serve media files
from django.conf import settings
from django.conf.urls.static import static

from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register('records', views.RecordView, base_name='records')
router.register('centers', views.ServiceCenterView, base_name='centers')

urlpatterns = [
    path('', include(router.urls)),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
