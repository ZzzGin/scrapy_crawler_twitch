import json
import requests
from bs4 import BeautifulSoup

with open('.//mc_links_1.json') as data_file:
    mc_links = json.load(data_file)

# with open('.//mc_games_data.json') as exists:
#     exists_data = json.load(exists)

# mc_links ={"Papers, Please": "https://www.metacritic.com/game/pc/papers-please"}
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
results = {}
count_all = len(mc_links)
count = 0
# [releaseDate, metaScore, userScore, genreList, userReviews, criticReviews]
for gn, gl in mc_links.items():
    print(str(count)+"/"+str(count_all))
    try:
        # if gn in exists_data:
        #     counts += 1
        #     continue
        if "metacritic" in gl:
            r = requests.get(gl, headers = headers)
            data = r.text
            soup = BeautifulSoup(data, features="html.parser")
            rd_temp = soup.select(".release_data .data")
            if len(rd_temp)!=0:
                releaseDate = rd_temp[0].text
            else:
                releaseDate = "N/A"

            ms_temp = soup.select('span[itemprop=ratingValue]')
            if len(ms_temp)!=0:
                metaScore = ms_temp[0].text
            else:
                metaScore = "N/A"

            us_temp = soup.select("div.metascore_w.user")
            if len(us_temp)!=0:
                userScore = us_temp[0].text
            else:
                userScore = "N/A"

            # .product_genre .data
            gL_temp = soup.select(".product_genre .data")
            genreList = []
            if len(gL_temp)!=0:
                for item in gL_temp:
                    genreList.append(item.text)
            else:
                genreList = "N/A"

            uR_temp = soup.select(".user_review .review_section")
            userReviews = []
            if len(uR_temp)!=0:
                for item in uR_temp:
                    try:
                        user_score = item.select("div.metascore_w")[0].text
                        user_review = item.select("span.blurb")[0].text
                        userReviews.append([user_score, user_review])
                    except:
                        continue
            else:
                userReviews = "N/A"

            cR_temp = soup.select(".critic_review .review_section")
            criticReviews = []
            if len(cR_temp)!=0:
                for item in cR_temp:
                    try:
                        critic_score = item.select("div.metascore_w")[0].text
                        critic_review = item.select(".review_body")[0].text
                        criticReviews.append([critic_score, critic_review])
                    except:
                        continue
            else:
                criticReviews = "N/A"

            results[gn] = [releaseDate, metaScore, userScore, genreList, userReviews, criticReviews]
            print(gn + ": " + str(results[gn][0:3]))
            file = open('mc_games_data.json', 'w+', encoding='utf8')
            json.dump(results, file)
            file.close()
            count+=1
        else:
            results[gn] = ["N/A", "N/A", "N/A", "N/A", "N/A", "N/A"]
            count+=1
    except:
        results[gn] = ["N/A", "N/A", "N/A", "N/A", "N/A", "N/A"]
        count+=1
        continue


    