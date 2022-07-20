from django.forms import ModelForm
from .models import *

class Questionform(ModelForm):
    class Meta:
        model=Question
        fields="__all__"


class Resultform(ModelForm):
    class Meta:
        model=Result
        fields=['status', 'note']      