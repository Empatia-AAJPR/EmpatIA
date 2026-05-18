from uuid import uuid4

from django.db import models


class Classroom(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    course = models.CharField(max_length=100)
    school = models.ForeignKey('Schools.School', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True, blank=True, default=None)

    class Meta:
        db_table = 'classroom'
