#!/usr/local/bin/python3
import sys
import spotipy.util as util

def main(user, uri):
	scope = "playlist-read-collaborative"
	token = util.prompt_for_user_token(user, scope)
	sp = spotipy.Spotify(auth=token, requests_session=True)
	pl = Playlist(sp, uri)
	pl.printAll()

if __name__ == "__main__":
	if len(sys.argv) != 3:
		print("Usage: playlist-metrics user playlist-uri")
		sys.exit()
	main(sys.argv[1], sys.argv[2])