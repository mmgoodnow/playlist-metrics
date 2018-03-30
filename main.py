#!/usr/local/bin/python3
import sys
import spotipy
import spotipy.util as util
from playlist import Playlist

class col:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def help():
	print()
	print(col.OKGREEN + "Commands:" + col.ENDC)
	print("    rankings - Show user rankings for this playlist")
	print("    exit - exit the program")
	print("    help - show this menu")
	print()

def main(user, uri):
	scope = "playlist-read-collaborative"
	token = util.prompt_for_user_token(user, scope)
	sp = spotipy.Spotify(auth=token, requests_session=True)
	pl = Playlist(sp, uri)
	
	while True:
		try: 
			line = input("Enter a command or type " + col.OKBLUE + "h" + col.ENDC +": ")
		except:
			print()
			break
		if line == "rankings":
			pl.rankings()
		elif line == "popular artists":
			pl.popularArtists()
		elif line == "common artists":
			pl.commonArtists()
		elif line == "favorite artists":
			pl.usersFavoriteArtists()
		elif line == "artists biggest adders":
			pl.usersFavoriteArtists()
		elif line == "help" or line == "h":
			help()
		elif line == "exit":
			print()
			break

if __name__ == "__main__":
	if len(sys.argv) != 3:
		print("Usage: playlist-metrics user playlist-uri")
		sys.exit()
	main(sys.argv[1], sys.argv[2])