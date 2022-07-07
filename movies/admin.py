from django.contrib import admin
from .models import Genre, Movie

# Register your models here.
# admin.site.register(Genre)
# admin.site.register(Movie)


class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class MovieAdmin(admin.ModelAdmin):
    # exclude = ('date_created',)  # This will exclude it from admin.
    # we don't need to do this bcz we have used auto_add_now
    list_display = ('id', 'title', 'number_in_stock', 'daily_rate')


admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin)
