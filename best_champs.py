from convert_functions import num_to_string, string_to_num
import ast

baseline = open("baseline_dataVladimir.txt", "r") # has dicts of appearances, wins and winrates for each champ number

lines = baseline.readlines()
print(lines)

wr = lines[2] #wr dict is this one
wr_dict = ast.literal_eval(wr)
apps_dict = ast.literal_eval(lines[0])
print(wr_dict)

print(num_to_string(str(1)))
print(string_to_num("Annie"))

list_of_champ_ints = []
for x in range(0,1000):
    if x in wr_dict and apps_dict[x]>200:
        list_of_champ_ints.append(x)
        print(wr_dict[x], num_to_string(str(x)))
print(list_of_champ_ints)
print(wr_dict)

wr_to_champ = {}
list_of_wr = []

for x in list_of_champ_ints:
    wr_dict[x] = round(wr_dict[x],6)
    list_of_wr.append(wr_dict[x])
    wr_to_champ[wr_dict[x]] = x

print(wr_to_champ)
print(sorted(list_of_wr, reverse=True))
sorted_wr = sorted(list_of_wr, reverse=True)

counter = 0
for x in sorted(list_of_wr, reverse=True):
    if counter<len(list_of_wr)/2:
        print(x, num_to_string(str(wr_to_champ[x])))
    else:
        break
    counter+=1