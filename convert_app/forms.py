from django import forms
from .models import GrayModel, FaceReadModel, AnimeModel, MosaicModel, FaceMosaicModel

class GrayForm(forms.ModelForm):
    class Meta:
        model = GrayModel
        fields = ('image',)

class FaceReadForm(forms.ModelForm):
    class Meta:
        model = FaceReadModel
        fields = ('image',)

class AnimeForm(forms.ModelForm):
    class Meta:
        model = AnimeModel
        fields = ('image',)

class MosaicForm(forms.ModelForm):
    class Meta:
        model = MosaicModel
        fields = ('image',)

class FaceMosaicForm(forms.ModelForm):
    class Meta:
        model = FaceMosaicModel
        fields = ('image',)
