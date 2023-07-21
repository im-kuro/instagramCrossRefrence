import toolkit, DONOTOPEN
from instagrapi import Client, exceptions

# login and init wrapper
clinetObj = Client()
clinetObj.login(DONOTOPEN.ACCOUNT_USERNAME, DONOTOPEN.ACCOUNT_PASSWORD)
 
obj = toolkit.tools(clinetObj)


obj.getAccountInfo("im_kuro_offical")


