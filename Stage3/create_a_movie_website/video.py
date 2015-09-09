import webbrowser

class Video():
    '''
    Main Class for all types of Video
    '''
    def __init__(self, title, poster_img, video_type, video_duration, trailer):
        self.type = video_type
        self.poster = poster_img
        self.duration = video_duration
        self.title = title
        self.trailer = trailer

    def play_trailer(self):
        webbrowser.open(self.trailer)