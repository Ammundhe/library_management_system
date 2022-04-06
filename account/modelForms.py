from django.forms import ModelForm
from django.contrib.auth import get_user_model
User = get_user_model()

class User_modelForms(ModelForm):
    class Meta:
        model=User
        fields=["first_name", "last_name", "password", "email"]