from django.contrib import admin
from .models import GrayModel, FaceReadModel, AnimeModel, MosaicModel, FaceMosaicModel

# Register your models here.
admin.site.register(GrayModel)
admin.site.register(FaceReadModel)
admin.site.register(AnimeModel)
admin.site.register(MosaicModel)
admin.site.register(FaceMosaicModel)