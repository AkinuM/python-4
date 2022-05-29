from django.contrib.auth.models import User
from django.db import models


class Waifu(models.Model):
    name = models.CharField('Name', max_length=20)
    rating = models.FloatField('Rating', default=0.0)
    description = models.TextField('Description')
    waifu_pic = models.ImageField('Waifu pic', upload_to="images/")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.id}'

    class Meta:
        verbose_name = 'Waifu'
        verbose_name_plural = 'Waifus'

class Rate(models.Model):
    value = models.IntegerField('Value')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    waifu = models.ForeignKey(Waifu, on_delete=models.CASCADE)

    def __str__(self):
        return self.value.__str__()

    def get_absolute_url(self):
        return f'/{self.waifu.id}'

    class Meta:
        unique_together = ('user', 'waifu')
        verbose_name = 'Rate'
        verbose_name_plural = 'Rates'

class Comment(models.Model):
    value = models.TextField('Value')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    waifu = models.ForeignKey(Waifu, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return f'/{self.waifu.id}'

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'