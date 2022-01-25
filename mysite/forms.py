from django.forms import ModelForm
from mysite.models import Patients


# Create the form class.
class ArticleForm(ModelForm):
    class Meta:
        model = Patients
        fields = ['name', 'age', 'pulse', 'date']



