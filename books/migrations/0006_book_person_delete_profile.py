# Generated by Django 4.0.2 on 2022-02-16 02:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books', '0005_alter_image_image_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='person',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
