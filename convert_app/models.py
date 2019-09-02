from django.db import models

class GrayModel(models.Model):
    image = models.ImageField(upload_to="uploads/")
    uploaded_at = models.DateTimeField(auto_now_add=True)
    gray_image = models.ImageField(default = 'gray/gray.jpg')