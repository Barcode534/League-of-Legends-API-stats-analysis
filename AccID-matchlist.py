import json
import requests
import time

print(time.time())

api_token = #REDACTED

def accid_to_matchlist():
    headers = {
        "Origin": "https://developer.riotgames.com",
        "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Riot-Token": api_token,
        "Accept-Language": "en-US,en;q=0.9",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
    }

    link_start = "https://euw1.api.riotgames.com/lol/match/v4/matchlists/by-account/"
    link_end = "?api_key=" + str(api_token)

    writing_file = open("Game IDs file.txt", "a+")

    with open("AccID.txt") as f:
        file = f.readlines()
        print(file)
        for line in file:
            #if counter>0:
            #    break
            line = line.rstrip("\n")
            print(line)
            link_middle = line
            link = link_start + link_middle + link_end
            response = requests.get(link, headers=headers)
            print(response)
            data = json.loads(response.content.decode('utf-8'))
            print(data)

            for entry in data:
                if entry == 'matches':
                    print(data[entry])
                    for game in data[entry]:
                        print(game)
                        for x in game:
                            if x == 'gameId':
                                print(game[x])
                                writing_file.write(str(game[x])+str("\n"))
                elif entry == "status":
                    time.sleep(75)
    writing_file.close()

output = accid_to_matchlist()