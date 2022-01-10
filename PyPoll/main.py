#Importing libraries
import os
import csv

#setting local path to csv file
election_data = os.path.join("election_data.csv")

#assigning list for name of candidates, number of votes and percentage of total votes respectively
Candidates = []
Number_of_Votes = []
Percentage_of_Votes = []

#setting initial for the total number of votes 
Total_Votes = 0

with open(election_data, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)

    for row in csvreader:

        #adding up our vote_counter 
        Total_Votes += 1 
        
        """ If the candidate is not in our list, result into our list, along with 
        If name is already in the list, then add a vote in respective result of voter. """

        if row[2] not in Candidates:
            Candidates.append(row[2])
            index = Candidates.index(row[2])
            Number_of_Votes.append(1)
        else:
            index = Candidates.index(row[2])
            Number_of_Votes[index] += 1
    #adding up Percentage_of_Votes list 
    for Votes in Number_of_Votes:
        Percentage = (Votes/Total_Votes) * 100
        Percentage = round(Percentage)
        Percentage = "%.3f%%" % Percentage
        Percentage_of_Votes.append(Percentage)   

    #looking for for winning candidate
    Winner = max(Number_of_Votes)
    index = Number_of_Votes.index(Winner)
    Winning_Candidate = Candidates[index]
#displaying results
print("Election Results")
print("_______________")
print(f"Total Votes: {str(Total_Votes)}")
print("_______________")
for i in range(len(Candidates)):
    print(f"{Candidates[i]}: {str(Percentage_of_Votes[i])} ({str(Number_of_Votes[i])})")
print("_______________")
print(f"Winner: {Winning_Candidate}")
print("_______________")

#Exporting .txt file
Analysis = open("Analysis.txt", "w")
line1 = "Election Results"
line2 = "_________________"
line3 = str(f"Total Votes: {str(Total_Votes)}")
line4 = str("_____________")
Analysis.write('{}\n{}\n{}\n{}\n'.format(line1, line2, line3, line4))
for i in range(len(Candidates)):
    line = str(f"{Candidates[i]}: {str(Percentage_of_Votes[i])} ({str(Number_of_Votes[i])})")
    Analysis.write('{}\n'.format(line))
line5 = "________________"
line6 = str(f"Winner: {Winning_Candidate}")
line7 = "________________"
Analysis.write('{}\n{}\n{}\n'.format(line5, line6, line7))
