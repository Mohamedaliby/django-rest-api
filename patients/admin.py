from django.contrib import admin

# Register your models here.
from satients.models import Patient, Tag, ServiceCenter

admin.site.register(Patient)
admin.site.register(Tag)
admin.site.register(ServiceCenter)
