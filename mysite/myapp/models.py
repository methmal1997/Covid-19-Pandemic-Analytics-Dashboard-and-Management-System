from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
from datetime import datetime, date


class Book1(models.Model):
    id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=30, default='', unique=True)
    age = models.IntegerField(default='')

    class Meta:
        db_table = 'Book1'

    def __str__(self):
        return f'{self.Name} | {self.age}'


class Hospital_beds(models.Model):
    id = models.AutoField(primary_key=True, default=1)
    District = models.CharField(max_length=30, default='', unique=True)
    Number_of_beds_per_1000 = models.IntegerField(default='')

    class Meta:
        db_table = 'Hospital_beds'

    def __str__(self):
        return f'{self.District} | {self.Number_of_beds_per_1000}'


class post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    how_donate = models.CharField(max_length=255)
    post_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('fund')


class District(models.Model):
    id = models.AutoField(primary_key=True)
    District = models.CharField(max_length=30, default='', unique=True)
    Cases = models.IntegerField(default='')
    Recovered = models.IntegerField(default='')
    Deaths = models.IntegerField(default='')

    class Meta:
        db_table = 'District'

    def __str__(self):
        return f'{self.District} | {self.Cases} | {self.Recovered} | {self.Deaths}'
