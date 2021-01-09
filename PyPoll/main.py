import os 
import csv
#csv path
csvpath = os.path.join('Resources','election_data.csv')

 
poll_data={}
total_votes = 0
with open(csvpath, 'r') as csvfile:
    csvread = csv.reader(csvfile)
    next(csvread, None)

    for row in csvread:
        total_votes += 1
        if row[2] in poll_data.keys():
            poll_data[row[2]] = poll_data[row[2]] + 1
        else:
            poll_data[row[2]] = 1 
    

candidates = []  
total_num_votes = []

for key, value in poll_data.items():
    candidates.append(key)
    total_num_votes.append(value)
  

percentage_votes =[]
for n in total_num_votes:
    percentage_votes.append(round(n/total_votes * 100, 1))
 

clean_data = list(zip(candidates, total_num_votes, percentage_votes))

winner_list = []
for name in clean_data:
    if max(total_num_votes) == name[1]:
        winner_list.append(name[0])
winner = winner_list[0]


print ("Election Results ")
print ("-------------------------------------------------------")
print("Total Votes  :  " + str(total_votes))
print("-------------------------------------------------------------\n")


print(candidates [0], "     " ":" + "   ",percentage_votes[0], "%", ":" + "   ", "(",total_num_votes[0],")")
print(candidates [1], "   " ":" + "   ",percentage_votes[1], "%", ":" + "   ", "(",total_num_votes[1],")")
print(candidates [2], "       " ":" + "   ",percentage_votes[2], "%", ":" + "   ", "(",total_num_votes[2],")")
print(candidates [3], " " ":" "   ",percentage_votes[3], "%", " :" + "   ", "(",total_num_votes[3],")")
print("------------------------------------------------------------\n")
print("Winner:" + " " + winner)
print("-------------------------------------------------------------\n")
 
    #analysis in  text file
   

with open('output.txt', 'w') as outtxt:
    
    outtxt.write("Election Results") 
    outtxt.write('\n' + "Total_votes" + str(total_votes)) 
    outtxt.write('\n' + str(candidates))
    outtxt.write('\n' + str(percentage_votes))
    outtxt.write('\n' + str(total_num_votes)) 
    outtxt.write('\n' + "Winner:" + winner)    
