# This ZIP file contains a project:
#	1. Travers the database from twitchTrend to gather all the game names;
#	2. Googles "[Game Name] + on metacritic" to get the URLs on MC;
#	3. Crawls MC URLs for information.
#
#
# Environments:
#	1. python 3.5.4
#	2. pip install beautifulsoup4
#	3. pip install requests
#	4. pip install openpyxl
# 	5. the pip list should be:
# 		Package           Version
# 		----------------- ----------
# 		astroid           2.1.0
# 		beautifulsoup4    4.6.3
# 		certifi           2018.11.29
# 		chardet           3.0.4
# 		clipboard         0.0.4
# 		colorama          0.4.1
# 		et-xmlfile        1.0.1
# 		idna              2.7
# 		isort             4.3.4
# 		jdcal             1.4
# 		lazy-object-proxy 1.3.1
# 		mccabe            0.6.1
# 		openpyxl          2.5.12
# 		pip               18.1
# 		pylint            2.2.2
# 		pyperclip         1.7.0
# 		requests          2.20.1
# 		setuptools        40.6.2
# 		six               1.11.0
# 		typed-ast         1.1.0
# 		urllib3           1.24.1
# 		wheel             0.32.3
# 		wrapt             1.10.11
#
#
# 1. gather all the game names；
#	python toJson.py 
# 2. get urls on MC:
#	python craw.py 
#	- then we get mc_links_1.json
# 3. get information:
#	python craw_mc.py
#	- then we get me_games_data.json
# 
# =====================================================================================
# Introduce the data gathered:
# 1. mc_links_1.json is a file contains a dictionary maps game names to urls:
#		The structure is:
#		- {"gameName": URL} type: {string: string}
#	 How to use:
import json

with open('.//mc_links_1.json') as data_file:
    mc_links = json.load(data_file)

print(mc_links["HITMAN"]) # an example
# =====================================================================================
#
# 2. mc_games_data.json is a file contains a dictionary about all the information for 
#		games exists in the data:
#		The structure is:
#		- {"gameName": "releaseTime", "mediaScore", "gamerScore", "gameGenre", "userReviews", "criticReviews"}
# 		Type：   |           |             |             |            |            |              |
#       - { string:     string,        string,       string,       list,        list,          list}
#    How to use:
import json

with open('.//mc_games_data.json') as data_file:
    gameData = json.load(data_file)

print("Release Time of 'HITMAN' is: " + gameData["HITMAN"][0])
print("MediaScore: " + gameData["HITMAN"][1])
print("GamerScore: " + gameData["HITMAN"][2])
print("GameGenre: " + str(gameData["HITMAN"][3]))
print("One of user's scrore and review: " + gameData["HITMAN"][4][0][0] + " " + gameData["HITMAN"][4][0][1])
print("One of media's scrore and review: " + gameData["HITMAN"][5][0][0] + " " + gameData["HITMAN"][5][0][1])