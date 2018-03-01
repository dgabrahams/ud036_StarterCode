class Movie():
    '''
      Creates an instance of the Movie Object.
      This object holds information about a film to be used later.
    '''
    def __init__(self, title, poster_image_url, trailer_youtube_url):
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
