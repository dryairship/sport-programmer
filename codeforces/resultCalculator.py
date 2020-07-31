#importing required libraries
import requests
import csv
import sys

#PART 1- input CSV -> string of handles (for parameter of API)
#and- input CSV -> dictOfHandles
with open(sys.argv[1], mode='r') as csv_file:
    stringOfHandles = ''
    dictOfHandles = {} #with key = handle; value = roll no.
    csv_reader = csv.reader(csv_file, delimiter=',')
    flag = 0
    for row in csv_reader:
        lowerCaseHandle = row[1].lower().strip()
        if(flag==0):
            stringOfHandles += lowerCaseHandle
            flag=1
            dictOfHandles[lowerCaseHandle] = row[0]
        else:
            stringOfHandles += ';'
            stringOfHandles += lowerCaseHandle
            dictOfHandles[lowerCaseHandle] = row[0]

#PART 2- API -> handles in order of their relative ranks 
parameters= {
    "contestId": sys.argv[2],
    "handles" : stringOfHandles,
    "showUnofficial": 'true'
}
URL = "https://codeforces.com/api/contest.standings"
page = requests.get(URL, params=parameters)

import json
tp = page.json()['result']['rows']

handlesInOrder = []
ranksInOrder = []

for person in tp:
    if person['party']['participantType'] not in ['OUT_OF_COMPETITION', 'CONTESTANT']:
        continue
    members_list = (person['party'])['members']
    handle = (members_list[0])['handle']
    absolute_rank = person['rank']
    handlesInOrder += [handle.lower()]
    ranksInOrder += [absolute_rank]
#print(handlesInOrder)

#Part 3- handlesInOrder + dictOfHandles -> CSV file with relative rank and roll no.
with open('ranks_for_contest.csv', mode='w') as final_file:
    file_writer = csv.writer(final_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    rank = 1
    count = 0
    for handle in handlesInOrder:
        if(count==0):
            file_writer.writerow([1, dictOfHandles[handle]])
            count+=1
            del dictOfHandles[handle]
        else:
            if(ranksInOrder[count]>ranksInOrder[count-1]):
                rank+=1
            file_writer.writerow([rank, dictOfHandles[handle]])
            count+=1
            del dictOfHandles[handle]
    for handle, roll_no in dictOfHandles.items():
        file_writer.writerow([10000, roll_no])
