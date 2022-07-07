from django.urls import path
from . import views

app_name = 'movies'  # we can reference urls using movies:

urlpatterns = [
    path('', views.index, name='index'),
    # as a best practice we name each endpoint, so we can address them, like movies:index
    path('<int:movie_id>', views.detail, name='detail')
]
