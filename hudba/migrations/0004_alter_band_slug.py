# Generated by Django 4.0.4 on 2022-05-28 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hudba', '0003_band_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='band',
            name='slug',
            field=models.SlugField(help_text='Use name of the band with only small letters and without spaces', null=True, verbose_name='Link'),
        ),
    ]
