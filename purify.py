import json
import webbrowser

with open('.//mc_links_4.json') as data_file:
    gameNameList = json.load(data_file)

for gn, gl in gameNameList.items():
    if "..." in gl:
        g = gn.replace(' ', '+')
        url = "https://www.google.com/search?q=" + g + "+on+metacritic"
        webbrowser.open_new_tab(url)
        gameNameList[gn] = input()
        file = open('mc_links_4.json', 'w+', encoding='utf8')
        json.dump(gameNameList, file)

print("Finish")
