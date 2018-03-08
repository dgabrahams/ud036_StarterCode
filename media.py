__author__ = "Daniel Abrahams"
__copyright__ = "Copyright 2018, Danel Abrahams"
__credits__ = ["Daniel Abrahams"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Daniel Abrahams"
__email__ = "10762864+dgabrahams@users.noreply.github.com"
__status__ = "Production"


class Movie():
    '''
      Creates an instance of the Movie Object.
      This object holds information about a film to be used later.
    '''
    def __init__(self, title, poster_image_url, trailer_youtube_url):
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
