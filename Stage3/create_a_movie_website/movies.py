from video import Video

class Movie(Video):
    '''
    Inherited class of Video for movies
    '''
    def __init__(self, title, poster, dur, trailer, rel_date, story_line):
        Video.__init__(self, title, poster, Movie.__name__, dur, trailer)
        self.release_date = rel_date
        self.storyline = story_line