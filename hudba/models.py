from django.db import models
from django.urls import reverse


def song_path(instance, filename):
    return "band/" + str(instance.band.id) + "/songs/" + filename


class Genre(models.Model):
    name = models.CharField(max_length=50,
                            unique=True,
                            verbose_name='Genre name',
                            help_text='Enter a band genre (e.g. pop, rock)')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Band(models.Model):
    title = models.CharField(max_length=200,
                             verbose_name="Name")
    release_date = models.DateField(blank=True,
                                    null=True,
                                    help_text="Please use the following format: <em>DD.MM.YYYY</em>.",
                                    verbose_name="Release date")
    poster = models.ImageField(blank=True,
                               verbose_name="Poster",
                               upload_to="posters/")
    genres = models.ManyToManyField(Genre, help_text='Select a genre for this band')

    class Meta:
        ordering = ["-release_date", "title"]

    def __str__(self):
        return f"{self.title}, year: {str(self.release_date.year)}"

    def get_absolute_url(self):
        return reverse('band-detail', args=[str(self.id)])


class Album(models.Model):
    title = models.CharField(max_length=200,
                             verbose_name="Name")
    last_update = models.DateTimeField(auto_now=True)
    release_date = models.DateField(blank=True,
                                    null=True,
                                    help_text="Please use the following format: <em>DD.MM.YYYY</em>.",
                                    verbose_name="Release date")
    band = models.ForeignKey(Band, on_delete=models.CASCADE)
    poster = models.ImageField(blank=True,
                               verbose_name="Poster",
                               upload_to="posters/")
    song_count = models.IntegerField(verbose_name="Number of songs")

    class Meta:
        ordering = ["-last_update"]

    def __str__(self):
        return f"{self.title}"


class Song(models.Model):
    title = models.CharField(max_length=200,
                             verbose_name="Title")
    last_update = models.DateTimeField(auto_now=True)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    genres = models.ManyToManyField(Genre, help_text='Select a genre for this band')

    class Meta:
        ordering = ["-last_update"]

    def __str__(self):
        return f"{self.title}"
