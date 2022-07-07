from django.db import models
# from django.utils import timezone


# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=255)  # from security point of view is also good, bcz prevents a 2 billion char

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=255)
    release_year = models.IntegerField()
    number_in_stock = models.IntegerField()
    daily_rate = models.FloatField()
    date_created = models.DateTimeField(auto_now_add=True)
    # date_created = models.DateTimeField(default=timezone.now)  #notice that we have passed a reference to the function
    # The options' auto_now, auto_now_add, and default are mutually exclusive. Only one of these options may be present.
    genre = models.ForeignKey(to=Genre, on_delete=models.CASCADE)
