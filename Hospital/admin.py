from django.contrib import admin

from Hospital.models import Institute, Person, Contact

# Register your models here.

admin.site.register(Person)
admin.site.register(Institute)
admin.site.register(Contact)
