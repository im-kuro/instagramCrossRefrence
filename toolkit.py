import json


class tools():
	def __init__(self, clientObj: dict) -> None:
		self.clientObj = clientObj    
    

    # INSTA STUFF
	def getAccountInfo(self, username: str) -> dict:
		return self.clientObj.user_info_by_username(username)
		
  
  
	def gatherFollowers(self, username):
		self.clientObj.user_followers(username)


	def gatherFollowing(self, username):
		# Gather following
		pass

	def gatherPosts(self, username):
		# Gather posts
		pass


	def gatherLikedBy(self, ):
		# Gather posts liked by users
		pass





	# MISC STUFF
 
	def saveToFile(self, path: str, data) -> bool:
		try:
			# Save data to file
			jsonDBObj = json.loads(open("sessions.json").read())
			jsonDBObj[path] = data
			# write changes to master database
			with open("sessions.json", "w") as masterDatabaseFile:
				masterDatabaseFile.write(json.dumps(jsonDBObj, indent=4))
			return True
		except Exception as e:
			return e

	def sessionSetup(self):
		pass


	def TFAHandler(self):
		pass
		# https://github.com/adw0rd/instagrapi - > additional ex.