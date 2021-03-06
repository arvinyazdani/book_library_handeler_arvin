# Generated by Django 4.0.2 on 2022-02-16 02:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0009_remove_person_book02_remove_person_book03'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='book02',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='givebook02', to='books.book'),
        ),
        migrations.AddField(
            model_name='person',
            name='book03',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='givebook03', to='books.book'),
        ),
        migrations.AlterField(
            model_name='person',
            name='book01',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='givebook01', to='books.book'),
        ),
    ]
