from django.urls import path
from .views import indexfunc, grayfunc, facereadfunc, animefunc, mosaicfunc

urlpatterns = [
    path('', indexfunc, name="index"),
    path('gray/', grayfunc, name="gray"),
    path('faceread/', facereadfunc, name="faceread"),
    path('anime/', animefunc, name="anime"),
    path('mosaic/', mosaicfunc, name="mosaic"),
]
