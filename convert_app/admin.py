from django.contrib import admin
from .models import GrayModel, FaceReadModel

# Register your models here.
admin.site.register(GrayModel)
admin.site.register(FaceReadModel)