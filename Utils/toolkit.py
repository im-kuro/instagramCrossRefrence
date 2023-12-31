#local imports
from . import helpers

import json, spacy, re, requests, random, time


class tools():
	def __init__(self, clientObj: dict) -> None:
		self.clientObj = clientObj    
		self.helpersObj = helpers.IOFuncs()
		self.reqSession = requests.Session()
	

	def getAccountInfo(self, username: str) -> dict:
		return self.clientObj.user_info_by_username(username)

	def followUser(self, pk: str) -> bool: 
		return self.clientObj.user_follow(pk)

	# MISC STUFF
 
	def saveToFile(self, path: str, data) -> bool:
		try:
			# Save data to file
			jsonDBObj = json.loads(open("Utils/sessions.json").read())
			jsonDBObj[path] = data
			# write changes to database
			with open("Utils/sessions.json", "w") as masterDatabaseFile:
				masterDatabaseFile.write(json.dumps(jsonDBObj, indent=4))
			return True
		except Exception as e:
			return e

	def __getSavedAccount__(self) -> str:
		try:
			return json.loads(open("Utils/sessions.json").read())["username"]
		except Exception as e:
			return e

	def __fix__(self) -> bool:
		"""This can be ran by runningn with -f to fix any possible issues with the tool

		Returns:
			bool: _description_
		"""
		try:
			# Save data to file
			jsonDBObj = json.loads(open("Utils/sessions.json").read())
			jsonDBObj["username"] = ""
			jsonDBObj["settingsDict"] = {}
			# write changes to database
			with open("Utils/sessions.json", "w") as masterDatabaseFile:
				masterDatabaseFile.write(json.dumps(jsonDBObj, indent=4))
			return True
		except Exception as e:
			return e




	def sessionSetup(self)-> bool:
		"""Used on startup to check if we have a session saved, if not we get account info and save it to file

		Returns:
			bool: worked or not
		"""
		# check if we have a session saved | if not, get account info | if so load session
		if json.loads(open("Utils/sessions.json").read())["settingsDict"] == {}:
			# get account info
			ACCOUNT_USERNAME = self.helpersObj.Default.getTextInput("Enter your username")
			ACCOUNT_PASSWORD = self.helpersObj.Default.getPassword("Enter your password")
			# log in
			self.clientObj.login(ACCOUNT_USERNAME, ACCOUNT_PASSWORD)
			self.helpersObj.Default.printSuccess(f"Login success!\n")

			if self.helpersObj.Default.getUserInput("Do you want to save your session (you can login without needing to input your user & pass)").lower() == "y":
				# Save the settings session to login faster in the future
				if self.saveToFile("settingsDict", self.clientObj.get_settings()) and self.saveToFile("username", ACCOUNT_USERNAME) and self.saveToFile("cookieDict", self.clientObj.cookie_dict) == True:			
					self.helpersObj.Default.printInfo("Saved settings to file!")
		
				else: 
					self.helpersObj.Default.printError(f"Failed to save settings to file!")
					return False
			else: 
				self.helpersObj.Default.printInfo("Not saving settings to file!")
				return True
		# else load session to login 
		else: 
			# load session
			self.clientObj.set_settings(json.loads(open("Utils/sessions.json").read())["settingsDict"])
			self.helpersObj.Default.printSuccess(f"loaded session!\n")
			return True



 
	# Main funcs

	def crossReferenceAccounts(self, targetPK: str) -> json:
		"""This will get followers & following to return the target's mutuals

		Args:
			targetPK (str): target insta ID

		Returns:
			json: json of the target's mutuals
		"""
		self.helpersObj.Default.printInfo(f"Please be patient, if the target has a lot of followers/following this could take 1-5 mins.")
		# get followers and following based on the count, we do this to lower api calls (hopefully idk lol)
		userFollowers = self.clientObj.user_followers_gql_chunk(targetPK)

		time.sleep(random.randint(10, 30))
  
		userFollowing = self.clientObj.user_following_v1(targetPK)
		mutualCount = 0
		jsonRes = {}
  
		# Assuming you have a list of users being followed stored in 'userFollowing'
		# Replace 'userFollowing' with the actual variable name containing the list of users being followed.
		userFollowing_usernames = [user.username for user in userFollowing]
  
		# Check if the target is following any of their followers
		for follower in userFollowers[0]:
			if follower.username in userFollowing_usernames:
				mutualCount += 1
				userInfo = self.clientObj.user_info_by_username(follower.username)
				jsonRes[follower.username] = {"userInfoDict": userInfo,"isMutuals": True}

				self.helpersObj.Default.printSuccess(f"found {mutualCount} mutual accounts!")
				time.sleep(random.randint(5, 15)) # this is purely for looks lmao
				print ("\033[A\033[A")
		print("\n")

		return {"mutuals": jsonRes, "mutualCount": mutualCount}




	def crossReferencePostsLikers(self, targetPK: str, tarMutuals: str) -> json:
		jsonRes = {}
		mutualLikerCount = 0
		mutualTagsCount = 0
		# get the target's posts
		targetMedias = self.clientObj.user_medias_gql(targetPK, 5)
  
		# check if the target has any posts
		if targetMedias == []:
			return None


		userTagsRes = {}
		# for each post, get the user tags and store it
		for media in targetMedias:
			for mediaTag in media.usertags:
				mutualTagsCount += 1
				userTagsRes[mediaTag.username] = {"userPK": mediaTag.pk, "mediaPK": mediaTag.pk}
   
		for media in targetMedias:
			time.sleep(random.randint(5, 10)) # this is purly for looks lmao
			likers = self.clientObj.media_likers(media.pk)
			for liker in likers:
				for mutual in tarMutuals["mutuals"]:

					if liker.username in mutual:
						jsonRes[liker.username] = {"mediaPK": media.pk, "mutualLikerPK": liker.pk}
      
						mutualLikerCount += 1
						self.helpersObj.Default.printSuccess(f"found {mutualLikerCount} mutuals that liked the post!")
						time.sleep(0.10) # this is purly for looks lmao
						print ("\033[A\033[A")
		print("\n")

		return {"mutualLikers": jsonRes, "mutualLikerCount": mutualLikerCount, "userTags":userTagsRes, "mutualTagsCount": mutualTagsCount}



	def pharseMisc(self, mutualToPharse: json) -> json:
		jsonRes = {}

		for mutualUsername, account_data in mutualToPharse.items():
			userInfoDict = account_data["userInfoDict"]
			userInfo = self.pharseBios(userInfoDict.biography)
			jsonRes[mutualUsername] = {"userInfo": userInfo}
			time.sleep(random.randint(5, 10))
		return jsonRes


	def pharseBios(self, userBio: str) -> json:
		"""This handles the pharsing of the user's bio to check for ages, places, names, schools ect. using spaCy

		Args:
			userBio (str): the users bio to be pharsed

		Returns:
			json: json response of the pharsed bio data
		"""
		# load the en lib
		nlp = spacy.load("en_core_web_sm")
		# Process the bio text using spaCy
		doc = nlp(userBio)
		# Matches numbers with 1 or 2 digits
		age_pattern = r'\b\d{1,2}\b'  
		# Initialize lists to store extracted entities
		counties = []
		abbreviations = []
		schools = []
		
		# Iterate through the entities identified by spaCy
		for ent in doc.ents:
			if ent.label_ == "GPE":  # Geo-Political Entity (e.g., countries, cities, states)
				counties.append(ent.text)
			elif ent.label_ == "ORG":  # Organizations
				schools.append(ent.text)
			elif ent.label_ == "LOC":  # Locations
				abbreviations.append(ent.text)
    
		ages = re.findall(age_pattern, userBio)
  
		return {"counties": counties, "abbreviations": abbreviations, "schools":schools, "ages": ages}



	def calcRating(self, mutuals: json, mutualLikers: json) -> json:
		mutualsCount = mutuals["mutualCount"]
		mutualLikersCount = mutualLikers["mutualLikerCount"]
		
		match mutualsCount:
			case 0:
				mutualsCountRating = 0
			case x if x >= 90:
				mutualsCountRating = 50
			case x if x >= 50:
				mutualsCountRating = 35
			case x if x >= 35:
				mutualsCountRating = 25
			case x if x >= 20:
				mutualsCountRating = 15
			case x if x >= 5:
				mutualsCountRating = 5

		match mutualLikersCount:
			case 0:
				mutualLikersRating = 0
			case x if x >= 90:
				mutualLikersRating = 50
			case x if x >= 50:
				mutualLikersRating = 35
			case x if x >= 35:
				mutualLikersRating = 25
			case x if x >= 20:
				mutualLikersRating = 25
			case x if x >= 5:
				mutualLikersRating = 5

		return mutualsCountRating + mutualLikersRating 
	
	def handlePrivateStatus(self, tarInfo: str) -> bool:
		"""Handles a target private acc

		Args:
			tarInfo (str): target info

		Returns:
			bool: worked or not
		"""
		if tarInfo.is_private == True:
			userInput = self.helpersObj.Default.getUserInput("This account is private. Do you want to request to follow them? (if you have already followed them and they accepted press ENTER.)").lower()
			if userInput == "y":
				self.toolkitObj.followUser(tarInfo.pk)
				self.helpersObj.Default.printError(f"Attempted to follow {tarInfo.username}")
				self.helpersObj.Default.printInfo(f"Come back later when they accept :(")
				exit(0)
			elif userInput == "":
				return True
			else:  
				self.helpersObj.Default.printInfo(f"Please choose an account thats not private.")
				exit(0)
		







