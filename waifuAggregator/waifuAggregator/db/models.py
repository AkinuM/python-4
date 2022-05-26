from django.db import models

class pegs(models.Model):
    name = models.TextField('Name')
    weight = models.IntegerField('Weight')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/db/{self.id}'

    class Meta:
        verbose_name = 'PEG'
        verbose_name_plural = 'PEGS'