import json
import requests
import time

print(time.time())

api_token = #REDACTED

def summid_to_accid():
    headers = {
        "Origin": "https://developer.riotgames.com",
        "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Riot-Token": api_token,
        "Accept-Language": "en-US,en;q=0.9",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
    }

    link_start = "https://euw1.api.riotgames.com/lol/summoner/v4/summoners/"
    link_end = "?api_key=" + str(api_token)

    with open("Names collected.txt") as f:
        file = f.readlines()
        print(file)
        for line in file:
            line = line.rstrip("\n")
            link_middle = line
            link = link_start + link_middle + link_end
            response = requests.get(link, headers=headers)
            print(response)
            data = json.loads(response.content.decode('utf-8'))
            print(data)

            for entry in data:
                print(entry)
                print(data[entry])
                if entry == "accountId":
                    file_write = open("AccID.txt", "a+")
                    file_write.write(data[entry]+"\n")
                    file_write.close()
                elif entry == "status":
                    time.sleep(70)

output = summid_to_accid()