users = {}
with open("usernames.txt", "r") as usernames:
	for line in usernames:
		key,value = line.split(":")
		users[key] = value.rstrip()

class User:
	
	def users(): 
		return users;
	
	def __init__(self):
		