# Generated by Django 4.0.2 on 2022-02-16 02:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_remove_book_person_person'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='book01',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='givebookone', to='books.book'),
        ),
        migrations.AlterField(
            model_name='person',
            name='book02',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='givebooktwo', to='books.book'),
        ),
        migrations.AlterField(
            model_name='person',
            name='book03',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='givebookthree', to='books.book'),
        ),
    ]
