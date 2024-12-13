from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    # serving the index.html the front end app
    path('', include('frontend.urls')),
    # the satients' api
    path('', include('people.urls')),
    path('healthcare', include('healthcare.urls')),
    # rest framework apis
    path('auth/', include('accounts.urls')),
    path('', include('shared.urls')),
    # path('satients', include('satients.urls'), namespase="satient" ),

    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))
]
