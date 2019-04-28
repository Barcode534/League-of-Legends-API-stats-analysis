import json

file = open("Champ_names_dicts.txt", "r")

lines = file.readlines()
name_to_id = lines[0].rstrip("\n")
name_to_id = name_to_id.replace("'", "\"")
name_to_id_dict = json.loads(name_to_id)

id_to_name = lines[1].replace("'", "\"")
id_to_name_dict = json.loads(id_to_name)


def num_to_string(num):
    return id_to_name_dict[str(num)]

def string_to_num(string):
    return name_to_id_dict[str(string)]

