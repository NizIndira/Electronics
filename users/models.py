from django.contrib.auth.models import AbstractUser
from django.db import models

from django.conf import settings


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')

    first_name = models.CharField(max_length=50, verbose_name='имя', **settings.NULLABLE)
    last_name = models.CharField(max_length=50, verbose_name='фамилия', **settings.NULLABLE)
    phone = models.CharField(max_length=35, verbose_name='телефон', **settings.NULLABLE)
    city = models.CharField(max_length=50, verbose_name='город', **settings.NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('email',)

    def __str__(self):
        return self.email
