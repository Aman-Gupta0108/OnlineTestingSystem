# Generated by Django 4.2.7 on 2024-07-13 08:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0005_result_examname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='result',
            name='attempt',
        ),
    ]