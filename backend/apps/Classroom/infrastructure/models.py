from django.db import models


class Classroom(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    course = models.CharField(max_length=100)
    school = models.ForeignKey('Schools.School', on_delete=models.CASCADE)
    nucleos_group = models.ForeignKey(
        'Schools.NucleosGroup', on_delete=models.CASCADE
    )
    create_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True, default=None)

    class Meta:
        db_table = 'classroom'
