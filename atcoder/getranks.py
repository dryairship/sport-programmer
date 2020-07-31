import json
import csv
from scrape import gen_json
from sys import argv

usernames = []
dictOfHandles = {}
with open(argv[1],'r') as f:
    fr = csv.reader(f, delimiter=',')
    for row in fr:
        usernames.append(row[1].strip())
        dictOfHandles[row[1].strip()] = row[0].strip()

print(dictOfHandles)
contest = argv[2]
gen_json(contest)

with open('ranklist.json', 'r') as f:
    data = json.load(f)


handlesInOrder = []
ranksInOrder = []

ranks = []

data = data["StandingsData"]
for i in data:
    if (i['UserScreenName'] in usernames):
        handlesInOrder += [i['UserScreenName']]
        ranksInOrder += [i['Rank']]

doneRolls = []

with open('ranks_for_contest.csv', mode='w') as final_file:
    file_writer = csv.writer(final_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    rank = 1
    count = 0
    for handle in handlesInOrder:
        if(count==0):
            file_writer.writerow([1, dictOfHandles[handle]])
            count+=1
            doneRolls.append(dictOfHandles[handle])
            del dictOfHandles[handle]
        else:
            if(ranksInOrder[count]>ranksInOrder[count-1]):
                rank+=1
            file_writer.writerow([rank, dictOfHandles[handle]])
            count+=1
            doneRolls.append(dictOfHandles[handle])
            del dictOfHandles[handle]
    for handle, roll_no in dictOfHandles.items():
        if roll_no not in doneRolls:
            doneRolls.append(roll_no)
            file_writer.writerow([10000, roll_no])
