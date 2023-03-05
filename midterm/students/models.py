from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=255, null=False)
    surname = models.CharField(max_length=255, null=False)
    year_of_study = models.IntegerField()

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Student'

    def _str_(self):
        return 'ID: {}, Name: {}'.format(self.id, self.name)
