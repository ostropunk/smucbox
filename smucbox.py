import tekore as tk
from pathlib import Path


class Smucbox():
    '''Class for creating a smucbox-instance.'''

    def __init__(self, configfile='config.txt'):
        self.configfile = self.check_config(configfile)
        self.conf = tk.config_from_file(configfile)

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
    smucbox


if __name__ == '__main__':
    main()
