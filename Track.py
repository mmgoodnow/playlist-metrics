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
