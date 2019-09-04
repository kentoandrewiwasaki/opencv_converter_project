from django.db import models

class GrayModel(models.Model):
    image = models.ImageField(upload_to="uploads/")
    gray_image = models.ImageField(default = 'gray/gray.jpg')

class FaceReadModel(models.Model):
    image = models.ImageField(upload_to="uploads/")
    faceread_image = models.ImageField(default = 'faceread/faceread.jpg')

class AnimeModel(models.Model):
    image = models.ImageField(upload_to="uploads/")
    anime_image = models.ImageField(default = 'anime/anime.jpg')

class MosaicModel(models.Model):
    image = models.ImageField(upload_to="uploads/")
    mosaic_image = models.ImageField(default = 'mosaic/mosaic.jpg')