from django.forms import modelform_factory
from mysite.models import Patients
from django import forms


form_model = modelform_factory(Patients, fields=('name', 'age', 'pulse', 'date'))

class UniverseForm(forms.Form):
    # SUBJECT_CHOICES = (
    #     (1, 'Web Development'),
    #     (2, 'System Programming'),
    #     (3, 'Data Science')
    # )

    name = forms.CharField()
    age = forms.IntegerField()
    pulse = forms.IntegerField()
    date = forms.DateField()
    # subject = forms.CharField(choices=SUBJECT_CHOICES)