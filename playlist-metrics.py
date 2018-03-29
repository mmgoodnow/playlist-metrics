#!/usr/local/bin/python3
import sys
import spotipy
import spotipy.util as util


class Track: 
	def __init__(self):
		h = 3

class Playlist:
	def __init__(self):
		b = 3

def main(user):
	scope = "playlist-read-collaborative" 
	id = "e86e2ab5847548598d0a3ef04a25af8f"
	secret = "1e382cad77c240d8822360970f4b064d"
	redir = "http://localhost"
	token = util.prompt_for_user_token(user, scope, id, secret, redir)
	
	sp = spotipy.Spotify(auth=token, requests_session=True)
	print(sp.user("kilometers_"))
	
if __name__ == "__main__":
	main("kilometers_")