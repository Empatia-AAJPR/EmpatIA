from django.db import models


class School(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    name = models.CharField(max_length=80)
    cnpj = models.CharField(max_length=20, null=False)
    logo = models.ImageField(upload_to='logos')
    gre = models.CharField(max_length=60)

    class Meta:
        db_table = 'schools'


class NucleosGroup(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    name = models.CharField(max_length=100)
    school = models.ForeignKey(
        'Schools.School',
        on_delete=models.CASCADE,
    )
