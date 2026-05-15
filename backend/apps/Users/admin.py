from django.contrib import admin

from apps.Users.infrastructure.models import Coordinator, Director, Student


admin.site.register(Student)
admin.site.register(Coordinator)
admin.site.register(Director)
