# Generated by Django 4.2.2 on 2023-06-08 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to='blog'),
        ),
        migrations.AddField(
            model_name='post',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='blog'),
        ),
        migrations.AddField(
            model_name='post',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='blog'),
        ),
        migrations.AddField(
            model_name='post',
            name='image4',
            field=models.ImageField(blank=True, null=True, upload_to='blog'),
        ),
        migrations.DeleteModel(
            name='Photo',
        ),
    ]