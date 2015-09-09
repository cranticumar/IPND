from video import Video
 
class Tvseries(Video):
    '''
    Inherited class of Video for TV series
    '''
    def __init__(self, title, poster_img, dur, trailer, series_start, series_end,
                 number_of_seasons, number_of_episodes, plot_summary):
        Video.__init__(self, title, poster_img, Tvseries.__name__, dur, trailer)
        self.start_date = series_start
        self.end_date = series_end
        self.seasons = number_of_seasons
        self.episodes = number_of_episodes
        self.plot = plot_summary