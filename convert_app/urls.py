from django.urls import path
from .views import indexfunc, grayfunc

urlpatterns = [
    path('index/', indexfunc, name="index"),
    path('gray/', grayfunc, name="gray"),
]
