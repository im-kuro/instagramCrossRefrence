
#local imports
import Utils.toolkit as toolkit, Utils.helpers as helpers
# non local
from instagrapi import Client, exceptions
import requests, os, time, random, argparse

argParser = argparse.ArgumentParser(description='Instagram cross refrence tool')

argParser.add_argument('-f', '--fix', help='fix any issues with the session, if you run into any API errors or somthing thats isnt handled in the code you can run with -f/--fix to fix any possible issues', action='store_true')

parsedArgObj = argParser.parse_args()

def main(tarUsername: str) -> bool:
	helpersObj.Default.printInfo(f"Gathering target account info => {tarUsername}")

	# get target account info (dict)
	tarInfo = toolkitObj.getAccountInfo(tarUsername)
	# print target account info
	helpersObj.Default.printArgsInfo(Target_Username=tarInfo.username, Target_PK=tarInfo.pk, Target_Followers=tarInfo.follower_count, Target_Following=tarInfo.following_count)

	# handle target account status
	toolkitObj.handlePrivateStatus(tarInfo)
 
 	# sleep to avoid ratelimit
	time.sleep(random.randint(10, 30))

	# find mutals
	mutuals = toolkitObj.crossRefrenceAccounts(tarInfo.pk)
	exit(0)
 
	time.sleep(random.randint(15, 30))
	tarPosts = toolkitObj.gatherPosts(tarInfo.pk)
	print(tarPosts)

	time.sleep(random.randint(15, 30))

	
	# compare data to see if the account is real or not


	# give rating on how real the account is
	helpersObj.Default.printSuccess(f"Target account rating: {accsRes + postsRes}")







if __name__ == '__main__':
    # check for os type to clear past output
	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')
	# init wrapper
	clientObj = Client()
    # mainly for input/output
	helpersObj = helpers.IOFuncs()
	# i init the toolkit here because we need the account obj to be passed in (yes im sure theres a better way to do this)
	toolkitObj = toolkit.tools(clientObj)

	# banner and other bullshit
	for _ in helpersObj.Default.banner.splitlines():
		print(_)
		time.sleep(0.1)
	helpersObj.Default.printInfo("Welcome to Kuro's Instagram cross refrence tool!")
	helpersObj.Default.printInfo("This tool will allow you to cross refrence a target's followers, following, and posts to see how real an account is")

	# check if sessions need to be fixed
	if parsedArgObj.fix:
		helpersObj.Default.printInfo("Fixing session...")
		if toolkitObj.__fix__():
			helpersObj.Default.printSuccess("Session fixed! You can now log in again.")
		else: helpersObj.Default.printError(f"Session error! Unable to fix session.")
		

 
 	# get target username
	target = helpersObj.Default.getTextInput("Enter the target username you want info on")

	try:  
		# check if we have a session saved | if not, get account info | if so load session
		toolkitObj.sessionSetup()
	
		# start main func
		main(target)
	except exceptions.BadPassword: helpersObj.Default.printError("Bad password!")
	except exceptions.ClientNotFoundError: helpersObj.Default.printError("The username used to login was not found!")
	except exceptions.ChallengeRequired: helpersObj.Default.printError("Challenge error! Please log in o the web and try again.")
	except requests.exceptions.HTTPError: helpersObj.Default.printError("Request error! Could be any issue with the request. Please log in on the web to see any possible issues.")
	except exceptions.ChallengeUnknownStep: helpersObj.Default.printError("Challenge error! Please log in on the web and try again.")
	except Exception as e: helpersObj.Default.printError(f"Unknown error! ERROR: {e}")







