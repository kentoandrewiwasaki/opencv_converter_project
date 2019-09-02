from django import forms
from .models import GrayModel

class GrayForm(forms.ModelForm):
    class Meta:
        model = GrayModel
        fields = ('image',)