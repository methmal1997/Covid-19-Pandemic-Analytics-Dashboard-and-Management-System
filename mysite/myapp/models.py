from django.db import models


class Book1(models.Model):

    Name = models.CharField(max_length=30,default='')
    age = models.IntegerField(default='')

    class Meta:
        db_table = 'Book1'