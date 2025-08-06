class Music():
    def __init__(self,name,artist,release,genre,sound):
        self.name=name
        self.artist=artist
        self.release=release
        self.genre=genre
        self.sound=sound
    def music_info(self):
        print(f"name={self.name},artist={self.artist},release={self.release},genre={self.genre},sound={self.sound}")
 
class Album(Music):
    album=""
    price=0
    def __init__(self):
        self.album="various album"
        self.price=3000

song=Music("a","b",2000,"c","%%%%%%%%")
song.music_info()

a=Album()
