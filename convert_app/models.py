from django.db import models

class GrayModel(models.Model):
    image = models.ImageField(upload_to="input/gray")
    gray_image = models.ImageField(default = 'output/gray/gray.jpg')

class FaceReadModel(models.Model):
    image = models.ImageField(upload_to="input/faceread")
    faceread_image = models.ImageField(default = 'output/faceread/faceread.jpg')

class AnimeModel(models.Model):
    image = models.ImageField(upload_to="input/anime")
    anime_image = models.ImageField(default = 'output/anime/anime.jpg')

class MosaicModel(models.Model):
    image = models.ImageField(upload_to="input/mosaic")
    mosaic_image = models.ImageField(default = 'output/mosaic/mosaic.jpg')

class FaceMosaicModel(models.Model):
    image = models.ImageField(upload_to="input/facemosaic")
    facemosaic_image = models.ImageField(default = 'output/facemosaic/facemosaic.jpg')