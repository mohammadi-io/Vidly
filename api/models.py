from tastypie.resources import ModelResource
from movies.models import Movie


# Create your models here.
class MovieResource(ModelResource):
    class Meta:
        excludes = ['date_created']
        queryset = Movie.objects.all()
        resource_name = 'movies'
