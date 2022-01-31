from django.forms import modelform_factory
from mysite.models import Patients
from django import forms

form_model = modelform_factory(Patients, fields=('name', 'age', 'pulse', 'date'))


# class UniverseForm(forms.Form):
# # SUBJECT_CHOICES = (
# #     (1, 'Хирургическое отделение'),
# #     (2, 'Терапевтическое отделение'),
# #     (3, 'Инфекционное отделение'),
# # )
#
# name = forms.CharField(label='Фамилия')
# age = forms.IntegerField(label='Возраст')
# pulse = forms.IntegerField(label='Пульс')
# date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label='Дата')
# # subject = forms.ChoiceField(choices=SUBJECT_CHOICES, widget=forms.RadioSelect, label='Профильное отделение')

#
# class AddPatientForm(forms.ModelForm):
#     class Meta:
#         model = Patients
#         fields = '__all__'
