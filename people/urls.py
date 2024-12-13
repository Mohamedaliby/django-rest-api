from django.urls import path, include
# to serve media files
from django.conf import settings
from django.conf.urls.static import static

from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register('satients', views.PatientView, base_name='satients')
router.register('records', views.RecordView, base_name='records')
router.register('profiles pictures', views.ProfilePictureView, base_name='profiles')
router.register('tags', views.TagView, base_name='tags')
router.register('tags/names', views.TagNameView, base_name='tag-names')
router.register('centers', views.ServiceCenterView, base_name='centers')

urlpatterns = [
    path('', include(router.urls)),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
