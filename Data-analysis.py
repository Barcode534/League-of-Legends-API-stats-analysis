import time
from convert_functions import num_to_string, string_to_num

counter = 0
app_dict = {}
wins_dict = {}
wr_dict = {}
teammate = input("Enter teammate's champion (capital first letter, Wukong = MonkeyKing)")
champ_num = string_to_num(str(teammate))
print(champ_num)


with open("uncorrupted.txt", "r") as f:
    lines = f.readlines()
    print(lines)
    for line in lines:
        if counter>70000:
            break
        list = []
        line = line.rstrip("\n")
        counter+=1
        line = line.split("][")
        data_list = []
        for x in line:
            x= x.lstrip("[")
            x= x.rstrip("]")
            data_list.append(x)
        team_1 = []
        team_2 = []
        team_1_result = []
        team_2_result = []
        team_1.append(data_list[0].split(","))
        team_2.append(data_list[1].split(","))
        team_1_result.append(max(data_list[2].split(",")))
        team_2_result.append(max(data_list[3].split(",")))
        team_1 = team_1[0]
        team_2 = team_2[0]
        for x in range(0,len(team_1)):
            team_1[x] = int(team_1[x])
            team_2[x] = int(team_2[x])
        for y in range(0, len(team_1_result)):
            team_1_result[y] = int(team_1_result[y])
            team_2_result[y] = int(team_2_result[y])
        print(team_1, team_2, team_1_result, team_2_result)
        data_teams = [team_1, team_2]
        data_results = [team_1_result, team_2_result]

        for x in range(0,len(data_teams)):
            print("data team[x] : " + str(data_teams[x]))
            for y in range(0,len(team_1)):
                print(data_teams[x][y])
                if int(champ_num) in data_teams[x]:
                    if data_teams[x][y] in app_dict:
                        app_dict[data_teams[x][y]] +=1
                    else:
                        app_dict[data_teams[x][y]] = 1
                    if data_teams[x][y] in team_1 and team_1_result[0]==1:
                        if data_teams[x][y] in wins_dict:
                            wins_dict[data_teams[x][y]] +=1
                        else:
                            wins_dict[data_teams[x][y]] = 1
                    if data_teams[x][y] in team_2 and team_2_result[0]==1:
                        if data_teams[x][y] in wins_dict:
                            wins_dict[data_teams[x][y]] +=1
                        else:
                            wins_dict[data_teams[x][y]] = 1

        print("apps: " + str(app_dict))
        print("wins: " + str(wins_dict))

        for x in range(0,1000):
            if x in app_dict and app_dict[x]>0 and x:
                if x not in wins_dict:
                    wins_dict[x] = 0
                wr_dict[x] = wins_dict[x]/app_dict[x]
        print("wr: " + str(wr_dict))

output = open("baseline_data" + teammate + ".txt", "w")
output.write(str(app_dict) + "\n" + str(wins_dict) + "\n" + str(wr_dict))
