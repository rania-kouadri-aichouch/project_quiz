from django.forms import ModelForm
from .models import *

class Questionform(ModelForm):
    class Meta:
        model=Question
        fields="__all__"