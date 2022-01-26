from django.forms import ModelForm, modelform_factory
from mysite.models import Patients


form_model = modelform_factory(Patients, fields=('name', 'age', 'pulse', 'date'))
