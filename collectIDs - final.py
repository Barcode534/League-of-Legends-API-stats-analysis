import json
import requests
import time

#print(time.time())

api_token = ##REDACTED
link = "https://euw1.api.riotgames.com/lol/league/v4/challengerleagues/by-queue/RANKED_SOLO_5x5?api_key=" + api_token
link_start = "https://euw1.api.riotgames.com/lol/league/v4/"
link_middle = ""
link_end = "leagues/by-queue/RANKED_SOLO_5x5?api_key=" + api_token
rank = ["challenger", "grandmaster", "master"]

def website_info():
    headers = {
    "Origin": "https://developer.riotgames.com",
    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
    "X-Riot-Token": api_token,
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
}
    response = requests.get(link, headers=headers)
    print(response)

    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None

file_appendage = input("Enter file name appendage: ")

for r in rank:
    link_middle = r
    print(link_start + link_middle + link_end)
    link = link_start + link_middle + link_end
    web = website_info()
    # file = open("Names "+str(time.time())+".txt", "w+", encoding="utf-8")
    file = open("Names collected" + str(file_appendage) + ".txt", "a+", encoding="utf-8")
    for key in web:
        if key == "entries":
            list = web[key]
            print(list)
            for entry in list:
                print(entry)
                for thing in entry:
                    if thing == "summonerId":
                        # print("thing: " + str(thing))
                        print("entry[thing]: " + str(entry[thing]))
                        file.write(entry[thing] + "\n")
    file.close()


