from user import *
class Track:
	def __init__(self, json):
		self.user = users.get(json.get("added_by").get("id"))
		self.user.addTrack(self)
		track = json.get("track")
		self.name = track.get("name")
		self.artists = list(art.get("name") for art in track.get("artists"))
		self.album = track.get("album").get("name")
	
	def print(self):
		print("User: " + self.user.realName())
		print("Artists:" + str(self.artists))
		print("Name: " + self.name)
		print("Album: " + self.album)
