import json
import requests
import time

api_token = #REDACTED

def gameIDs_to_data():
    headers = {
        "Origin": "https://developer.riotgames.com",
        "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Riot-Token": api_token,
        "Accept-Language": "en-US,en;q=0.9",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
    }

    link_start = "https://euw1.api.riotgames.com/lol/match/v4/matches/"
    link_end = "?api_key=" + str(api_token)

    with open("non-dup gameIDs.txt") as f:
        file = f.readlines()
        print(file)
        for line in file:
            line = line.rstrip("\n")
            print(line)
            link_middle = line
            link = link_start + link_middle + link_end
            print(link)
            response = requests.get(link, headers=headers)
            print(response)
            while response.status_code == 429:
                time.sleep(5)
                response = requests.get(link, headers=headers)
            data = json.loads(response.content.decode('utf-8'))
            print(data)
            team_1_list = []
            team_2_list = []
            team_1_result = []
            team_2_result = []
            for entry in data:
                print(entry)
                if entry == "participants":
                    for x in data[entry]:
                        print("x is: " + str(x))
                        print(x['teamId'])
                        if x['teamId'] == 100:
                            team_1_list.append(x['championId'])
                            if x['stats']['win'] == True:
                                team_1_result.append(1)
                                team_2_result.append(0)
                            elif x['stats']['win'] == False:
                                team_1_result.append(0)
                                team_2_result.append(1)
                        else:
                            team_2_list.append(x['championId'])
                        for y in x:
                            if y == "stats":
                                print("x[y] is: " + str(x[y]))
            print(team_1_list, team_2_list, team_1_result, team_2_result)
            with open("datacollection_TESTING.txt", "a+") as writing_file:
                writing_file.write(str(team_1_list) + str(team_2_list) + str(team_1_result) + str(team_2_result) +"\n")

output = gameIDs_to_data()