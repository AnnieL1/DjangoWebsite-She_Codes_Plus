# Generated by Django 4.1.3 on 2022-12-17 00:23

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0007_delete_customeruser'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsstory',
            name='fave_by',
            field=models.ManyToManyField(blank=True, related_name='favourites', to=settings.AUTH_USER_MODEL),
        ),
    ]
