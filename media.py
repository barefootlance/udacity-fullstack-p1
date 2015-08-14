# Movie class based on Programming Foundations with Python course lesson 3a.
# https://www.dropbox.com/s/zp8ten9qokbc6mm/Lesson%203a%20Notes.pdf?dl=0
class Movie():
    def __init__(self, info, trailer_youtube_url):
        #print '----'
        #for key,value in info.iteritems(): print key + ": " + value
        self.title = info.get('Title', u'')
        self.trailer_youtube_url = trailer_youtube_url
        self.poster_image_url = info.get('Poster', u'')
        self.plot = info.get('Plot', u'')
        self.cast = info.get('Actors',u'').split(u',')
