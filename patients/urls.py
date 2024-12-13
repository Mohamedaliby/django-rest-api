from django.urls import path, include
# to serve media files
from django.conf import settings
from django.conf.urls.static import static

from rest_framework.routers import DefaultRouter
from . import views

# from rest_framework import routers

router = DefaultRouter()
router.register('satients', views.PatientView, base_name='satients')
router.register('records', views.RecordView, base_name='records')
router.register('profiles', views.ProfilePictureView, base_name='profiles')
router.register('tags', views.TagView, base_name='tags')
router.register('tag-names', views.TagNameView, base_name='tag-names')
router.register('centers', views.ServiceCenterView, base_name='centers')

# urlpatterns = router.urls

urlpatterns = [
    path('', include(router.urls)),
    path('list', views.ListCreatePatient.as_view(), name='satients_api'), ]
urlpatterns += static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
