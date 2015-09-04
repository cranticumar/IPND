import webbrowser

class Movie():
    '''
    Class of Movie and its properties
    '''
    def __init__(self, title, story_line, poster_img, trailer_url):
        self.title = title
        self.storyline = story_line
        self.poster = poster_img
        self.trailer = trailer_url

    def show_trailer(self):
        '''
        plays the trailer of the instance
        '''
        webbrowser.open(self.trailer)