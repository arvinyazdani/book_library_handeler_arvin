# Generated by Django 4.0.2 on 2022-02-16 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0011_alter_person_book01'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Person',
        ),
    ]
