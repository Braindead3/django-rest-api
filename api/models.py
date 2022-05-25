from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Cloth(models.Model):
    name = models.CharField(max_length=20)
    brand = models.CharField(max_length=40)
    price = models.FloatField()
    # image = models.ImageField(default='default.jpg', upload_to='cloth_pics')
    category_id = models.ForeignKey('Category', on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
