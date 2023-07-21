from colorama import Fore, Style, init
import getpass

init()

# the class for the input/output functions
class IOFuncs:

	class Default:
		def printError(Error: str) ->  str: print(f"{Fore.RED} + [ERROR] --> {Error}{Style.RESET_ALL}") 
		def printSuccess(Success: str) ->  str: print(f"{Fore.GREEN} + [SUCCESS] --> {Success}{Style.RESET_ALL}") 
		def printInfo(Info: str) ->  str: print(f"{Fore.BLUE} + [INFO] --> {Info}{Style.RESET_ALL}") 
		def getUserInput(Input: str) ->  str: return input(f"{Fore.MAGENTA} + [INPUT] --> {Input} y/n: {Style.RESET_ALL}") 
		def getMultiOptionInput(Input: str, q1, q2, q3) ->  str: return input(f"{Fore.MAGENTA} + [INPUT] --> {Input} ({q1} or {q2} or {q3}): {Style.RESET_ALL}") 
		def getTextInput(Input: str) -> str: return input(f"{Fore.MAGENTA} + [INPUT] --> {Input}: {Style.RESET_ALL}")
		def getPassword(Input: str) -> str: return getpass.getpass(f"{Fore.MAGENTA} + [INPUT] --> {Input}: {Style.RESET_ALL}")
		banner = fr"""{Fore.RED}
  
 ____  __.                     .___                 __           ________    _________.___ __________________
|    |/ _|__ _________  ____   |   | ____   _______/  |______    \_____  \  /   _____/|   |\      \__    ___/
|      < |  |  \_  __ \/  _ \  |   |/    \ /  ___/\   __\__  \    /   |   \ \_____  \ |   |/   |   \|    |   
|    |  \|  |  /|  | \(  <_> ) |   |   |  \\___ \  |  |  / __ \_ /    |    \/        \|   /    |    \    |   
|____|__ \____/ |__|   \____/  |___|___|  /____  > |__| (____  / \_______  /_______  /|___\____|__  /____|   
        \/                              \/     \/            \/          \/        \/             \/         

		Developed by @Kuro/@devkuro
  		"""