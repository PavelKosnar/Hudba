# Generated by Django 4.0.4 on 2022-05-06 22:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hudba', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='band',
            name='rate',
        ),
    ]
