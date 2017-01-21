import webbrowser

class Movie():
    '''This class provides a way to store movie related information.'''
    """
         title: This contains title of movie.
         storyline: This contains description of movie.
         poster_image_url: This containes url of poster image for a movie.
         trailer_youtube_url: This contains youtube url for trailer of a movie.
    """
    
    def __init__(self,movie_title,movie_storyline,poster_image,trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
