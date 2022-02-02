from django.db import models
from django.utils.datetime_safe import datetime


class Patients(models.Model):
    """
    Первоначальная модель где будет фамилия, возраст и пульс
    для тренировки вычисляемых полей.
    """
    name = models.CharField(max_length=30, null=True, blank=True, verbose_name='Фамилия пациента')
    age = models.IntegerField(null=True, blank=True, verbose_name='Возраст')
    note = models.TextField(null=True, blank=True, verbose_name='Дневник')
    pulse = models.IntegerField(null=True, blank=True, verbose_name='Пульс')
    date = models.DateTimeField(null=True, blank=True, default=datetime.now, verbose_name='Дата')

    def __str__(self):
        return self.name
