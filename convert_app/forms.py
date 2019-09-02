from django import forms
from .models import GrayModel, FaceReadModel

class GrayForm(forms.ModelForm):
    class Meta:
        model = GrayModel
        fields = ('image',)

class FaceReadForm(forms.ModelForm):
    class Meta:
        model = FaceReadModel
        fields = ('image',)