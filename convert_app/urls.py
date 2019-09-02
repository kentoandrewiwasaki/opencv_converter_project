from django.urls import path
from .views import indexfunc, grayfunc, facereadfunc

urlpatterns = [
    path('', indexfunc, name="index"),
    path('gray/', grayfunc, name="gray"),
    path('faceread/', facereadfunc, name="faceread")
]
