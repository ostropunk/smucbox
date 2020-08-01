import tekore as tk
from pathlib import Path


class Smucbox():
    '''Class for creating a smucbox-instance.'''

    def __init__(self, configfile='config.txt'):
        self.configfile = self.check_config(configfile)
        self.conf = tk.config_from_file(configfile)
        self.user_token = tk.prompt_for_user_token(
                            *self.conf, scope=tk.scope.every)

    def check_config(self, configfile):
        config_path = Path(configfile)
        if config_path.exists() is False:
            client_id = input('Enter Client Id: ')
            client_secret = input('Enter Client Secret: ')
            redirect_url = input('Enter Redirect url: ')

            tk.config_to_file(configfile, [client_id, client_secret,
                              redirect_url])

        return configfile


def main():
    smucbox = Smucbox()
    
    spotify = tk.Spotify(smucbox.user_token)
    artist = spotify.current_user_top_artists(limit=1).items[0]
    related = spotify.artist_related_artists(artist.id)
    followed = spotify.followed_artists(limit=50)
    followed = spotify.all_items(followed)
    followed_ids = [f.id for f in followed]

    print(f'Artists related to {artist.name}:')
    for a in related:
        f = ' F -' if a.id in followed_ids else 'NF -'
        print(f, a.name)


if __name__ == '__main__':
    main()
