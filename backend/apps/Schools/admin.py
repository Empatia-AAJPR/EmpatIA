from django.contrib import admin

from apps.Schools.infrastructure.models import NucleosGroup, School


admin.site.register(School)
admin.site.register(NucleosGroup)
