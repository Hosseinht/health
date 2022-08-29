from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Glucose(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='glucose')
    gerät = models.CharField(max_length=200)
    seriennummer = models.CharField(max_length=200)
    aufzeichnungstyp = models.PositiveSmallIntegerField(default=0)
    glukosewert = models.PositiveSmallIntegerField(help_text='Verlauf mg/dL')
    gerätezeitstempel = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'Glucose'
        verbose_name_plural = 'Glucose'

    def __str__(self):
        return self.user.user.username