# Generated by Django 3.0.3 on 2020-02-18 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='gallery/static/images/no-img.jpg', upload_to='gallery'),
        ),
    ]
