from django.contrib.auth.models import User
from django.db import models

class Waifu(models.Model):
    name = models.CharField('Name', max_length=50)
    description = models.TextField('Description')
    waifu_pic = models.ImageField('Preview')
    rating = models.IntegerField('Rating')

class Rate(models.Model):
    value = models.IntegerField('Value')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    waifu = models.ForeignKey(Waifu, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'waifu')

class Comment(models.Model):
    value = models.TextField('Value')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    waifu = models.ForeignKey(Waifu, on_delete=models.CASCADE)