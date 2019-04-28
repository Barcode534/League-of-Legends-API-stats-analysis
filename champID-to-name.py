import requests, json

link = "http://ddragon.leagueoflegends.com/cdn/9.8.1/data/en_US/champion.json"

names_to_id_dict = {}
id_to_names_dict = {}

response = requests.get(link)
print(response)
data = json.loads(response.content.decode('utf-8'))

for x in data:
    print(type(data[x]))
    if isinstance(data[x], dict):
        print(data[x])
        y = data[x]
        for z in y:
            names_to_id_dict[z] = y[z]['key']
            id_to_names_dict[y[z]['key']] = z
            print(y[z]['key'])

print(names_to_id_dict)
print(id_to_names_dict)

output = open("Champ_names_dicts.txt", "w")
output.write(str(names_to_id_dict) + "\n" + str(id_to_names_dict))
