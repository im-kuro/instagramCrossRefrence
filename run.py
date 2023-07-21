
#local imports
import toolkit, helpers
# non local
from instagrapi import Client, exceptions
import requests, json


def main(tarUsername: str) -> bool:
	helpersObj.Default.printInfo(f"Gathering target account info => {tarUsername}")
	
	# get target account info (dict)
	tarInfo = toolkitObj.getAccountInfo(tarUsername)
	print(tarInfo)
	helpersObj.Default.printInfo(f"Target account info => {tarInfo['username']}\nUser PK => {tarInfo['pk']}\nUser is private => {tarInfo['is_private']}\nMedia Count => {tarInfo['media_count']}\nFollower Count => {tarInfo['follower_count']}\nFollowing Count => {tarInfo['following_count']}\n\n")







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
		# log in
		clientObj.login(ACCOUNT_USERNAME, ACCOUNT_PASSWORD)
	# else load session to login
	
	else: 
		print(json.loads(open("sessions.json").read())["settingsDict"])
		Client.set_settings(settings={
        "settingsDict": {
			"timezone_offset": -14400,
			"device_settings": {
				"app_version": "269.0.0.18.75",
				"android_version": 26,
				"android_release": "8.0.0",
				"dpi": "480dpi",
				"resolution": "1080x1920",
				"manufacturer": "OnePlus",
				"device": "devitron",
				"model": "6T Dev",
				"cpu": "qcom",
				"version_code": "314665256"
			},
			"user_agent": "Instagram 269.0.0.18.75 Android (26/8.0.0; 480dpi; 1080x1920; OnePlus; 6T Dev; devitron; qcom; en_US; 314665256)",
			"uuids": {},
			"locale": "en_US",
			"country": "US",
			"country_code": 1,
			"ig_u_rur": "null",
			"ig_www_claim": "null"
			}})
	

	# i init the toolkit here because we need the account obj to be passed in
	toolkitObj = toolkit.tools(clientObj)
	
	if helpersObj.Default.getUserInput("Do you want to save your session (you can login without needing to input your user & pass)").lower() == "y":
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










