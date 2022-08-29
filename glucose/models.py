from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()


class Glucose(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    gerät = models.CharField(max_length=200)
    seriennummer = models.CharField(max_length=200)
    aufzeichnungstyp = models.PositiveSmallIntegerField(default=0)
    glukosewert = models.PositiveSmallIntegerField(help_text='Verlauf mg/dL')

    def __str__(self):
        return self.user

    class Meta:
        verbose_name = 'Glucose'
        verbose_name_plural = 'Glucose'
