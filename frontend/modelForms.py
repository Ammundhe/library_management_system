from django.forms import ModelForm
from library.models import Issue


class Issue_modelform(ModelForm):
    class Meta:
        model=Issue
        fields=["student", "book", "issued", "returned", "return_date"]
        