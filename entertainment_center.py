#calling the constructor media.Movie() to instantiate movie objects. 
#You've given movies their own custom data structure by defining the movie class and constructor, 
#and now these objects can be stored in a list data structure. This list of movies is what the 
#open_movies_page() function needs as input in order to build the HTML file, so you can display your website.

import media
import fresh_tomatoes

movie_list = {
		"starship_troopers" : {
			"title" : "Starship Troopers",
			"poster_image_url" : "https://images-na.ssl-images-amazon.com/images/M/MV5BNThlOTFhOGEtZjE2NC00MzMzLThkYWItZjlkNWNlMDAzMGZkXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SY1000_CR0,0,732,1000_AL_.jpg",
			"trailer_youtube_url" : "https://www.youtube.com/watch?v=zPYuV_jGk7M"
		},
		"catch_22" : {
			"title" : "Catch-22",
			"poster_image_url" : "https://images-na.ssl-images-amazon.com/images/M/MV5BZjM2M2IzY2QtMWU4My00NmFlLWIwNDUtZmNiZjNmMDhmYThjXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
			"trailer_youtube_url" : "https://www.youtube.com/watch?v=Unn8fgs8fao"
		},
		"star_wars_empire" : {
			"title" : "Star Wars: The Empire Strikes Back",
			"poster_image_url" : "https://images-na.ssl-images-amazon.com/images/M/MV5BYmU1NDRjNDgtMzhiMi00NjZmLTg5NGItZDNiZjU5NTU4OTE0XkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_SY1000_CR0,0,641,1000_AL_.jpg",
			"trailer_youtube_url" : "https://www.youtube.com/watch?v=UHjpuWtFT1M"
		}
}
# print movie_list

movies = []

for item in movie_list:
	movie = media.Movie(movie_list[item]["title"], movie_list[item]["poster_image_url"], movie_list[item]["trailer_youtube_url"])
	movies.append(movie)

# print movie_list["starship_troopers"]["trailer_youtube_url"]
print movies

#starship_troopers = media.Movie("Starship Troopers", "https://images-na.ssl-images-amazon.com/images/M/MV5BNThlOTFhOGEtZjE2NC00MzMzLThkYWItZjlkNWNlMDAzMGZkXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SY1000_CR0,0,732,1000_AL_.jpg", "https://www.youtube.com/watch?v=zPYuV_jGk7M")
#starship_troopers.show_info()

#catch_22 = media.Movie("Catch-22", "https://images-na.ssl-images-amazon.com/images/M/MV5BZjM2M2IzY2QtMWU4My00NmFlLWIwNDUtZmNiZjNmMDhmYThjXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SY1000_CR0,0,674,1000_AL_.jpg", "https://www.youtube.com/watch?v=Unn8fgs8fao")
#catch_22.show_info()

#star_wars_empire = media.Movie("Star Wars: The Empire Strikes Back", "https://images-na.ssl-images-amazon.com/images/M/MV5BYmU1NDRjNDgtMzhiMi00NjZmLTg5NGItZDNiZjU5NTU4OTE0XkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_SY1000_CR0,0,641,1000_AL_.jpg", "https://www.youtube.com/watch?v=UHjpuWtFT1M")
#star_wars_empire.show_info()

#movies = [starship_troopers, catch_22, star_wars_empire]
fresh_tomatoes.open_movies_page(movies)
