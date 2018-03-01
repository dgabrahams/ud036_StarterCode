class Movie():
	def __init__(self, title, poster_image_url, trailer_youtube_url):
		print("Movie Constructor Called")
		self.title = title
		self.poster_image_url = poster_image_url
		self.trailer_youtube_url = trailer_youtube_url

	def show_info(self):
		print("title - "+self.title)
		print("poster_image_url - "+self.poster_image_url)
		print("trailer_youtube_url - "+self.trailer_youtube_url)

'''
movie.title
movie.poster_image_url
trailer_youtube_id
movie.trailer_youtube_url
'''