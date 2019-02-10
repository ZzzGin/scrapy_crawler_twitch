import json
import requests
from bs4 import BeautifulSoup

with open('.//gameNameList_2.json') as data_file:
    gameNameList = json.load(data_file)

mc_links = {}
counter = 0
all_counter = len(gameNameList)

for gameName in gameNameList:
    gn = gameName.replace(' ', '+')
    url = "https://www.google.com/search?q=" + gn + "+on+metacritic"
    print("Searching Google on \"" + url + "\"")
    r = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data, features="html.parser")
    resultList = soup.select("div cite")
    if len(resultList) != 0:
        mc_links[gameName] = resultList[0].text
        print(mc_links[gameName])
    else:
        mc_links[gameName] = "No results"
        print("No results.")
    counter += 1
    print(str(counter) + "/" + str(all_counter) + " is completed..")

    # if counter == 10:
    #     print(mc_links)
    #     break

file = open('mc_links_2.json', 'w+', encoding='utf8')
json.dump(mc_links, file)
