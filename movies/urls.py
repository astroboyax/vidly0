from django.urls import path
from . import views

# movies/   # is root
# movies/details

app_name = 'movies'  # sparing the "movies_ ""

urlpatterns = [
    path('', views.index, name='index'),  # movies_index
    path('<int:movie_id>', views.detail, name='detail')  # movies_detail
]
