# Generated by Django 4.1.6 on 2023-03-17 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_textmodel_delete_savefilemodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textmodel',
            name='text',
            field=models.TextField(default=''),
        ),
    ]
