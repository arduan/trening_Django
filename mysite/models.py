from django.db import models


class Patients(models.Model):
    """
    Первоначальная модель где будет фамилия, возраст и пульс
    для тренировки вычисляемых полей.
    """
    name = models.CharField(max_length=30, null=True, blank=True, verbose_name='Фамилия пациенте')
    age = models.IntegerField(null=True, blank=True, verbose_name='Возраст')
    pulse = models.IntegerField(null=True, blank=True, verbose_name='Пульс')
    date = models.DateTimeField(null=True, blank=True, verbose_name='Дата')

    def __str__(self):
        return self.name
