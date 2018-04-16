import sys
import spotipy
import re
import track
import users
from track import Track
from users import User

class Playlist:
	def __init__(self, sp, uri):
		match = re.match(r'spotify:user:(.+):playlist:(.+)', uri)
		user = match.group(1)
		plid = match.group(2)
		mkt = "US"
		fields = "items(added_by.id,track(uri,name,album.name,artists.name))"
		limit = 100
		json = sp.user_playlist_tracks(user, plid, "total", limit, 0, mkt)
		total = json.get("total")
		i = 0
		self.tracks = []
		print()
		for off in range(0, total, limit):
			json = sp.user_playlist_tracks(user, plid, fields, limit, off, mkt)
			for i in range(len(json.get("items"))):
				self.tracks.append(Track(json.get("items")[i]))
			sys.stdout.write("\rFetching data: %d%%" 
			% (100 * min(off + 100, total) / total))
			sys.stdout.flush()
		print()
	
	def printAll(tracks):
		for track in tracks:
			track.print()
			print()
		
	def size(self):
		c = 0
		for track in self.tracks:
			c += 1
		print("Size: " + str(c))
	
	def rankings(self):
		rankings = {}
		
		# initialize all rankings to 0
		for key,value in users.items():
			rankings[key] = 0
		
		# sort track list by user
		sorted_list = sorted(self.tracks, key = lambda t: t.user)
		
		# counting sort second half
		i = 0
		for user,ntracks in rankings.items():
			c = 0
			while i < len(sorted_list) and user == sorted_list[i].user:
				c += 1
				i += 1
			rankings[user] = c
		ptl = []
		for key,value in rankings.items():
			ptl.append([users[key],value])
		
		ptl.sort(key = lambda r: r[1], reverse = True)
		
		print("\nRankings: ")
		for pair in ptl:
			if pair[1] > 0:
				spacer = ":" + (" " * (15 - len(pair[0]) - len(str(pair[1]))))
				print("    " + pair[0] + spacer + str(pair[1]))
	
	# top 20 artists, users per artist, display {artist : number of users}
	def popularArtists(self):
		print("Not Implemented")
		
	# top 20 artists, number of songs, display {artist : number of songs}
	def commonArtists(self):
		art_dic = {}
		for song in self.tracks:
			for artist in song.artists:
				try: art_dic[artist] += 1
				except: art_dic[artist] = 1
		art_ranks = \
		sorted(art_dic.items(), reverse=True, key=lambda tup: tup[1])[0:19]
		for pair in art_ranks:
			spacer = ":" + (" " * (25 - len(pair[0]) - len(str(pair[1]))))
			print("    " + pair[0] + spacer + str(pair[1]))
		
	
	# most added artist per user
	def favorites(self):
		print("Not Implemented")
	
	# top 20 artists, users per artist, display {artist : most popular user}
	def artistsFavoriteUsers(self):
		print("Not Implemented")
	

