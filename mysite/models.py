from django.db import models
from django.utils.datetime_safe import datetime


# The Patients class is a model that defines the fields of a table in the database
class Patients(models.Model):
    """
    Первоначальная модель где будет фамилия, возраст и пульс
    для тренировки вычисляемых полей.
    """
    analise = models.ForeignKey('Analise', on_delete=models.CASCADE, null=True, verbose_name="Анализы")
    name = models.CharField(max_length=30, null=True, blank=True, verbose_name='Фамилия пациента')
    age = models.IntegerField(null=True, blank=True, verbose_name='Возраст')
    note = models.TextField(null=True, blank=True, verbose_name='Дневник')
    pulse = models.IntegerField(null=True, blank=True, verbose_name='Пульс')
    date = models.DateTimeField(null=True, blank=True, default=datetime.now, verbose_name='Дата')

    def get_absolute_url(self):
        return f'/create/{self.id}'

    def __str__(self):
        return self.name


# This is a class that represents a single instance of an Analise
class Analise(models.Model):
    """
    Модель анализов и гемодинамики.
    """

    date = models.DateTimeField(null=True, blank=True, db_index=True, verbose_name='Дата анализа')
    leukocyte = models.FloatField(null=True, blank=True, verbose_name='Лейкоциты')
    hemoglobin = models.IntegerField(null=True, blank=True, verbose_name='Гемоглобин')
    sys_ad = models.IntegerField(null=True, blank=True, verbose_name='Систолическое АД')
    dias_ad = models.IntegerField(null=True, blank=True, verbose_name='Диастолическое АД')

    def get_absolute_url(self):
        return f'/analise/{self.id}'

    def __str__(self):
        return '%s ' % (self.leukocyte)
