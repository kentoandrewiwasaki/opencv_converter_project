from django import forms
from .models import GrayModel, FaceReadModel, AnimeModel, MosaicModel

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
