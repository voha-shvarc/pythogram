# Generated by Django 3.2.4 on 2021-06-11 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20210611_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(null=True, related_name='related_post', to='posts.Like'),
        ),
    ]