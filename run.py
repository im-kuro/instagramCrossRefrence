
#local imports
import toolkit, helpers
# non local
from instagrapi import Client, exceptions
import requests, json


def main(tarUsername: str) -> bool:

	helpersObj.Default.printInfo(f"Gathering target account info => {tarUsername}")
	
 
	# get target account info (dict)
	tarInfo = toolkitObj.getAccountInfo(tarUsername)








if __name__ == '__main__':
    # mainly for input/output
	helpersObj = helpers.IOFuncs()
 
	# banner and other bullshit
	print(helpersObj.Default.banner)
	helpersObj.Default.printInfo("Welcome to Kuro's Instagram cross refrence tool!")
	helpersObj.Default.printInfo("This tool will allow you to cross refrence a target's followers, following, and posts to see how real an account is.\n\n")

 
 	# get target username
	target = helpersObj.Default.getTextInput("Enter the target username you want info on")
 
	# login and init wrapper
	clientObj = Client()
	
	# check if we have a session saved | if not, get account info | 
	if json.loads(open("sessions.json").read())["settingsDict"] == {}:
		# get account info
		ACCOUNT_USERNAME = helpersObj.Default.getTextInput("Enter your username")
		ACCOUNT_PASSWORD = helpersObj.Default.getPassword("Enter your password")
		clientObj.login(ACCOUNT_USERNAME, ACCOUNT_PASSWORD)
	else: Client.set_settings(json.loads(open("sessions.json").read())["settingsDict"])
 

	# i init the toolkit here because we need the account obj to be passed in
	toolkitObj = toolkit.tools(clientObj)
	
	if helpersObj.Default.getTextInput("Do you want to save your session (you can login without needing to input your user & pass)").lower() == "y":
		# Save the settings session to login faster in the future
		if toolkitObj.saveToFile("settingsDict", clientObj.settings) == True:
			helpersObj.Default.printInfo("Saved settings to file!")
		else: helpersObj.Default.printError(f"Failed to save settings to file! Error: {toolkitObj.saveToFile('settingsDict', clientObj.settings())}")
	else: helpersObj.Default.printInfo("Not saving settings to file!")
	
	try:
		# start main func
		main(target)
	except exceptions.BadPassword: helpersObj.Default.printError("Bad password!")
	except exceptions.ClientNotFoundError: helpersObj.Default.printError("The username used to login was not found!")
	except exceptions.ChallengeRequired: helpersObj.Default.printError("Challenge error! Please log in o the web and try again.")
	except requests.exceptions.HTTPError: helpersObj.Default.printError("Request error! Could be any issue with the request. Please log in on the web to see any possible issues.")










