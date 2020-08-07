# smucbox


## What it is
 Code for creating a musicbox using spotipy (wrapper for spotify web api) and rfid-tags.
 
 
 ## What it does
 Uses a raspeberry pi with an mfc522 chip to read rfid tags that store playlist URI's. 
 The app sends a play request to the spotify api and tells it to start play the playlist 
 on your last used device (as long as it hasn't timed out).
 
 
 ## What you will need
 * A raspberry pi (tested on Raspberry Pi 4) with some kind of case.
 * A RFID RC522 module
 * Python libraries: spotipy, RPi.GPIO, mfrc522
 * A spotify premium account
 * A developer account on spotify (https://developer.spotify.com/)
 * A registered app with:
  * Client ID
  * Client Secret
  * Redirect URI (can be anything, like http://localhost:5000/callback/)
 
You vill need to store your credentials somehow. Write this in commandline and substitute
nessesary credentials.
 
export SPOTIPY_CLIENT_ID=client_id_here

export SPOTIPY_CLIENT_SECRET=client_secret_here

export SPOTIPY_REDIRECT_URI=redirect_uri_here

On Windows, use `SET` instead of `export` (does not work in PowerShell)
 
 
