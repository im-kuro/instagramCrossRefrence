
#local imports
import Utils.toolkit as toolkit, Utils.helpers as helpers
# non local
from instagrapi import Client, exceptions
import requests, os, time, random, argparse
from colorama import Fore

argParser = argparse.ArgumentParser(description='Instagram cross refrence tool')

argParser.add_argument('-f', '--fix', help='fix any issues with the session, if you run into any API errors or somthing thats isnt handled in the code you can run with -f/--fix to fix any possible issues', action='store_true')
argParser.add_argument('-a', '--savedAccount', help='show the account that is currently saved in the sessions', action='store_true')

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
	time.sleep(random.randint(10, 15))

	# find mutals | 25 points
	mutuals = toolkitObj.crossReferenceAccounts(tarInfo.pk)
	
	time.sleep(random.randint(10, 15))
 
	# cross refrence likers of posts & tags in thoes posts | 25 points
	tarPostLikers = toolkitObj.crossReferencePostsLikers(tarInfo.pk, mutuals)
	print(tarPostLikers)

	# cross refrence tags | 25 points



	# pharse accounts bio & hashtags for info & checking for common last names | 25 points
 
 

	# give rating on how real the account is
	#rating = mutuals["rate"] + tarPostLikers["rate"]
	#print(Fore.YELLOW + f"[Result] This account is most likely fake, if there where any mutuals found you can manually check them and the leads. {Fore.RED}RATING: {rating}% ")
	#elif x+z+y+q >= 50:




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
		
	# check if we have a saved account to print username
	if parsedArgObj.savedAccount:
		savedUsername = toolkitObj.__getSavedAccount__()
		if savedUsername != "": helpersObj.Default.printInfo(f"Saved account: {savedUsername}"); exit(0)
		else: helpersObj.Default.printError(f"There is no saved account!"); exit(0)
		

 
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
	except exceptions.UserNotFound: helpersObj.Default.printError("Username not found! Please enter a valid username.")
	except Exception as e: helpersObj.Default.printError(f"Unknown error! ERROR: {e}")







