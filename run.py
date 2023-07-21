
#local imports
import toolkit, helpers
# non local
from instagrapi import Client, exceptions
import requests, json, os


def main(tarUsername: str) -> bool:
	helpersObj.Default.printInfo(f"Gathering target account info => {tarUsername}")
	
	# get target account info (dict)
	tarInfo = toolkitObj.getAccountInfo(tarUsername)
	# print target account info
	helpersObj.Default.printArgsInfo(Target_Username=tarInfo.username, Target_PK=tarInfo.pk, Target_Followers=tarInfo.follower_count, Target_Following=tarInfo.following_count)

	# start extracting data (followers/following/posts likers)




	# compare data to see if the account is real or not
 



	# give rating on how real the account is
 
 






if __name__ == '__main__':
    # check for os type to clear past output
	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')

	######## objects #########
	##########################
	# init wrapper
	clientObj = Client()
    # mainly for input/output
	helpersObj = helpers.IOFuncs()
	# i init the toolkit here because we need the account obj to be passed in (yes im sure theres a better way to do this)
	toolkitObj = toolkit.tools(clientObj)

	
	# banner and other bullshit
	print(helpersObj.Default.banner)
	helpersObj.Default.printInfo("Welcome to Kuro's Instagram cross refrence tool!")
	helpersObj.Default.printInfo("This tool will allow you to cross refrence a target's followers, following, and posts to see how real an account is.\n\n")

 
 	# get target username
	target = helpersObj.Default.getTextInput("Enter the target username you want info on")

	# check if we have a session saved | if not, get account info | 
	if json.loads(open("sessions.json").read())["settingsDict"] == {}:
		# get account info
		ACCOUNT_USERNAME = helpersObj.Default.getTextInput("Enter your username")
		ACCOUNT_PASSWORD = helpersObj.Default.getPassword("Enter your password")
		# log in
		clientObj.login(ACCOUNT_USERNAME, ACCOUNT_PASSWORD)
  
  
		if helpersObj.Default.getUserInput("Do you want to save your session (you can login without needing to input your user & pass)").lower() == "y":
			# Save the settings session to login faster in the future
			if toolkitObj.saveToFile("settingsDict", clientObj.settings) == True:
				helpersObj.Default.printInfo("Saved settings to file!")
			else: helpersObj.Default.printError(f"Failed to save settings to file! Error: {toolkitObj.saveToFile('settingsDict', clientObj.settings())}")
		else: helpersObj.Default.printInfo("Not saving settings to file!")
	# else load session to login 
	else: 
		# load session
		clientObj.set_settings(json.loads(open("sessions.json").read())["settingsDict"])
	

	try:
		# start main func
		main(target)
	except exceptions.BadPassword: helpersObj.Default.printError("Bad password!")
	except exceptions.ClientNotFoundError: helpersObj.Default.printError("The username used to login was not found!")
	except exceptions.ChallengeRequired: helpersObj.Default.printError("Challenge error! Please log in o the web and try again.")
	except requests.exceptions.HTTPError: helpersObj.Default.printError("Request error! Could be any issue with the request. Please log in on the web to see any possible issues.")










