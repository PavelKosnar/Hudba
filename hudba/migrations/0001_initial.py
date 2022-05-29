import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Name')),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('release_date', models.DateField(blank=True,
                                                  help_text='Please use the following format: <em>DD.MM.YYYY</em>.',
                                                  null=True, verbose_name='Release date')),
                ('poster', models.ImageField(blank=True, upload_to='posters/', verbose_name='Poster')),
                ('song_count', models.IntegerField(verbose_name='Number of songs')),
            ],
            options={
                'ordering': ['-last_update'],
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a band genre (e.g. pop, rock)', max_length=50, unique=True,
                                          verbose_name='Genre name')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hudba.album')),
                ('genres', models.ManyToManyField(help_text='Select a genre for this band', to='hudba.Genre')),
            ],
            options={
                'ordering': ['-last_update'],
            },
        ),
        migrations.CreateModel(
            name='Band',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Name')),
                ('release_date', models.DateField(blank=True,
                                                  help_text='Please use the following format: <em>DD.MM.YYYY</em>.',
                                                  null=True,
                                                  verbose_name='Release date')),
                ('poster', models.ImageField(blank=True, upload_to='posters/', verbose_name='Poster')),
                ('rate', models.IntegerField(validators=[django.core.validators.MaxValueValidator(10),
                                                         django.core.validators.MinValueValidator(1)],
                                             verbose_name='Rate')),
                ('genres', models.ManyToManyField(help_text='Select a genre for this band', to='hudba.Genre')),
            ],
            options={
                'ordering': ['-release_date', 'title'],
            },
        ),
        migrations.AddField(
            model_name='album',
            name='band',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hudba.band'),
        ),
    ]
