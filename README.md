# Instagram account sifter

This tool is meant to cross refrence diffrent users followers and followings to find accounts 
that are following one user but not the other. As confusing as that sounds, it has a simple 
endgoal usage. It will give you a rating on how real the account is. This is useful for OSINT
automation. If you have a feeling you have the right account but you want to make sure it is,
use this tool to see what mutuals they have. If they have a lot of mutuals, they are probably 
real and you can use thoes mutals for more OSINT.


https://github.com/im-kuro/instagramCrossRefrence/assets/86091489/866abb01-7ad7-4340-8a5c-a8f011f069fd



## Please note
- Yes, its slow. But this is because instagram has tightened up their API so rate limits are common. if you happen to be rate limited just wait 12 hours and try again. If it still persists, try using a VPN thats not public or residential proxies. **Along with using -f to fix the saved session settings!!**
- Yes i know the data flow is shitty, i plan to get a working version out first then clean it up.
- If you have any code suggestions please open a pull request, i would love to see what you have to add.

## Installation
Download the code from github
```bash
~$ git clone https://github.com/im-kuro/instagramCrossRefrence/
```

cd into the directory
```bash
~$ cd instagramCrossRefrence
```

Install needed requirements
```bash
~$ pip install -r requirements.txt
```

run the program
```bash
~$ python3 run.py
```
