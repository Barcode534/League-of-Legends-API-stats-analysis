def gameids_to_data():
    writing_file = open("non-dup gameIDs.txt", "a+")
    games_list = []
    with open("Game IDs file.txt") as f:
        file = f.readlines()
        for line in file:
            line = line.rstrip("\n")
            if int(line) not in games_list:
                games_list.insert(-1,int(line))

    for game in games_list:
        writing_file.write(str(game)+"\n")

output = gameids_to_data()