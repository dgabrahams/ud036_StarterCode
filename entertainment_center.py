#calling the constructor media.Movie() to instantiate movie objects. 
#You've given movies their own custom data structure by defining the movie class and constructor, 
#and now these objects can be stored in a list data structure. This list of movies is what the 
#open_movies_page() function needs as input in order to build the HTML file, so you can display your website.

import media
import fresh_tomatoes

movie_list = {
  "starship_troopers": {
    "title": "Starship Troopers",
    "poster_image_url": "http://bit.ly/2HVCteF",
    "trailer_youtube_url": "https://www.youtube.com/watch?v=zPYuV_jGk7M"
  },
  "catch_22": {
    "title": "Catch-22",
    "poster_image_url": "http://bit.ly/2FFYe1n",
    "trailer_youtube_url": "https://www.youtube.com/watch?v=Unn8fgs8fao"
  },
  "star_wars_empire": {
    "title": "Star Wars: The Empire Strikes Back",
    "poster_image_url": "http://bit.ly/2GRez2A",
    "trailer_youtube_url": "https://www.youtube.com/watch?v=UHjpuWtFT1M"
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
