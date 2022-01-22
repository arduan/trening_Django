from django.db import models
from django.db.models import Max


class Patients(models.Model):
    """
    Первоначальная модель где будет фамилия, возраст и пульс
    для тренировки вычисляемых полей.
    """
    name = models.CharField(max_length=30, verbose_name='Фамилия пациенте')
    age = models.IntegerField(null=True, verbose_name='Возраст')
    pulse = models.IntegerField(null=True, verbose_name='Пульс')


    def __str__(self):
        return self.name