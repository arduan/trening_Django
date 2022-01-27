from django.forms import modelform_factory
from mysite.models import Patients
from django import forms


form_model = modelform_factory(Patients, fields=('name', 'age', 'pulse', 'date'))

class UniverseForm(forms.Form):
    SUBJECT_CHOICES = (
        (1, 'Хирургическое отделение'),
        (2, 'Терапевтическое отделение'),
        (3, 'Инфекционное отделение'),
    )

    name = forms.CharField()
    age = forms.IntegerField()
    pulse = forms.IntegerField()
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    subject = forms.ChoiceField(choices=SUBJECT_CHOICES, widget=forms.RadioSelect)