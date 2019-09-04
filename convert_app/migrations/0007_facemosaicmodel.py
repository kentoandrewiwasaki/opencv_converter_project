# Generated by Django 2.2.4 on 2019-09-04 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('convert_app', '0006_mosaicmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='FaceMosaicModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='uploads/')),
                ('facemosaic_image', models.ImageField(default='facemosaic/facemosaic.jpg', upload_to='')),
            ],
        ),
    ]
