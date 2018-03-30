#!/usr/local/bin/python3
import sys
import spotipy
import spotipy.util as util
import re


class Track:
	def __init__(self, json):
		self.user = json.get("added_by").get("id")
		track = json.get("track")
		self.name = track.get("name")
		self.artists = list(artist.get("name") for artist in track.get("artists"))
		self.album = track.get("album").get("name")
	
	def print(self):
		#print(self.user)
		#print(self.artists)
		print(self.name)
		#print(self.album)
		

class Playlist:
	def __init__(self, sp, uri):
		match = re.match(r'spotify:user:(.+):playlist:(.+)', uri)
		user = match.group(1)
		plid = match.group(2)
		mkt = "US"
		fields = "items(added_by.id,track(name,album.name,artists.name))"
		limit = 100
		json = sp.user_playlist_tracks(user, plid, "total", limit, 0, mkt)
		total = json.get("total")
		i = 0
		self.tracks = []
		for off in range(0, total, limit):
			json = sp.user_playlist_tracks(user, plid, fields, limit, off, mkt)
			for i in range(len(json.get("items"))):
				self.tracks.append(Track(json.get("items")[i]))
			sys.stdout.write("\rRequesting data: %d%%" 
			% (100 * min(off + 100, total) / total))
			sys.stdout.flush()
		print()
	def printAll(self):
		for track in self.tracks:
			track.print();
			
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