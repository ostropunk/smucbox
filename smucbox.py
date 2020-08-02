import spotipy
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522 as rc
from spotipy.oauth2 import SpotifyOAuth

scope = "user-library-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, cache_path='cache/cache.txt'))

results = sp.current_user_saved_tracks()

class Smucbox():
    '''Class for handling spotify connections.'''

    def __init__(self):
        '''Method for creating a smucbox'''
        self.client = self.make_client()
        self.user = self.client.current_user()
        

    def make_config_file(self):
        '''Method for creating a config file.'''
        pass
    
    def make_client(self):
        '''Method for creating a spotipy client.'''
        scope = "user-library-read, user-read-playback-state, user-modify-playback-state"
        
        return spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, cache_path='cache/cache.txt'))
    
    def get_uri(self):
        reader = rc()
        print('Read card:')
        try:
            id, text = reader.read()
        finally:
            GPIO.cleanup()
            
        return text.rstrip()
    
    def playback(self, uri):
        urilist = []
        urilist.append(uri)
        print(urilist)
        self.client.start_playback(context_uri=urilist)
    
    def run(self):
        while True:
            self.playback(self.get_uri())
            continue
        


if __name__ == '__main__':
    smucbox = Smucbox()
    smucbox.run()
