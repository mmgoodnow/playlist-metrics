class User:
	def __init__(self, username, name):
		self.username = username
		self.name = name
		self.tracks = []
	
	def addTrack(self, track):
		self.tracks.append(track)
	
	def realName(self):
		return self.name
	
	def printTracks(self):
		for track in self.tracks:
			track.print()
	
	def numTracks(self):
		return len(self.tracks)
		
	def favoriteArtist(self):
		art_dic = {}
		for song in self.tracks:
			for artist in song.artists:
				try: art_dic[artist] += 1
				except: art_dic[artist] = 1
		sortedList = sorted(art_dic.items(), reverse=True, key=lambda t: t[1])
		return sortedList[0]
		
users = {}
with open("usernames.txt", "r") as usernames:
	for line in usernames:
		key,value = line.split(":")
		users[key] = User(key, value.rstrip())