from django.db import models


# Create your models here.


class product(models.Model):
    description = models.TextField(null=False, blank=False)
    price = models.FloatField(null=False, blank=False)
    image = models.ImageField(upload_to='djangoburger/img', default='', null=False, blank='False')


    def __str__(self):
        return self.description
