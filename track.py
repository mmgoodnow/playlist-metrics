users = {}
with open("usernames.txt", "r") as usernames:
	for line in usernames:
		key,value = line.split(":")
		users[key] = value.rstrip()

class Track:
	def __init__(self, json):
		self.user = json.get("added_by").get("id")
		track = json.get("track")
		self.name = track.get("name")
		self.artists = list(artist.get("name") for artist in track.get("artists"))
		self.album = track.get("album").get("name")
	
	def print(self):
		print("User: " + self.user)
		print("Person: " + users.get(self.user))
		print("Artists:" + str(self.artists))
		print("Name: " + self.name)
		print("Album: " + self.album)
