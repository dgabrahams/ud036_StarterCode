
import media
import fresh_tomatoes

'''
    This file creates a Dictionary of movie files and associated meta data,
    creates a data structure of this dictionary in memory and then runs
    the fresh_tomatoes.open_movies_page function to initiate the
    application.
'''

__author__ = "Daniel Abrahams"
__copyright__ = "Copyright 2018, Danel Abrahams"
__credits__ = ["Daniel Abrahams"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Daniel Abrahams"
__email__ = "10762864+dgabrahams@users.noreply.github.com"
__status__ = "Production"


movie_list = {
  "starship_troopers": {
    "title": "Starship Troopers",
    "poster_image_url": "http://bit.ly/2HVCteF",
    "trailer_youtube_url": "hhttps://youtu.be/zPYuV_jGk7M"
  },
  "catch_22": {
    "title": "Catch-22",
    "poster_image_url": "http://bit.ly/2FFYe1n",
    "trailer_youtube_url": "https://youtu.be/Unn8fgs8fao"
  },
  "bad_boy_bubby": {
    "title": "Bad Boy Bubby",
    "poster_image_url": "http://bit.ly/2F7zjTD",
    "trailer_youtube_url": "https://youtu.be/YXZ4u2ZVWOc"
  }
}
movies = []

for item in movie_list:
    movie = media.Movie(
      movie_list[item]["title"],
      movie_list[item]["poster_image_url"],
      movie_list[item]["trailer_youtube_url"]
      )
    movies.append(movie)

fresh_tomatoes.open_movies_page(movies)
