import os
import csv
from typing import Counter
csvpath = os.path.join('Resources','election_data.csv')

Votes = []
Candidates = []
percent_votes = []
total_votes = 0


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_Header = next(csvfile)
    
    for row in csvreader:
        total_votes += 1
        if row[2] not in Candidates:
            Candidates.append(row[2])
            index = Candidates.index(row[2])
            Votes.append(1)
        else:
            index = Candidates.index(row[2])
            Votes[index] += 1

    for num_votes in Votes:
            percentage = (num_votes/total_votes) *100
            percentage = round(percentage)
            percentage = "%.3f" % percentage
            percent_votes.append(percentage)

    winner = max(Votes)
    index = Votes.index(winner)
    Winning_candidate = Candidates[index]


print("Election Results")
print("----------------------------------------------------")
print(f"Total Votes: {total_votes}")
print("----------------------------------------------------")
for i in range(len(Candidates)):
    print(f"{Candidates[i]}: {str(percent_votes[i])}% {str(Votes[i])}")
print("----------------------------------------------------")
print(f"Winner: {Winning_candidate}")
print("----------------------------------------------------")



output_file = os.path.join('Analysis', 'analysis.txt')
with open(output_file, "w") as txtfile:
    txtfile.write("Election Results" + "\n")
    txtfile.write("----------------------------------------------------" + "\n")
    txtfile.write(f"Total Votes: {total_votes}" + "\n")
    txtfile.write("----------------------------------------------------" + "\n")
    for i in range(len(Candidates)):
        txtfile.write(f"{Candidates[i]}: {str(percent_votes[i])}% {str(Votes[i])}" + "\n")
    txtfile.write("----------------------------------------------------" + "\n")
    txtfile.write(f"Winner: {Winning_candidate}" + "\n")
    txtfile.write("----------------------------------------------------" + "\n")