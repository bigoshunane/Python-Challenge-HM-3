#Importing modules
import os
import csv

#setting local path to data csv file
budget_data = os.path.join("budget_data.csv")

#setting initials for variables; total_months,total_profit/losses(PL) et.al
Dates = []
Profits = []
Total_Months = 0
Value = 0
Change = 0
Total_PL= 0

#opening and reading csv file
with open(budget_data, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

#row_header 
    csv_header = next(csvreader)

#reading next first row and keeping track of changes
    first_row = next(csvreader)
    Total_Months += 1
    Total_PL += int(first_row[1])
    Value = int(first_row[1])

#looping via each rowS
    for row in csvreader:

#keeping track of dates
        Dates.append(row[0])

#calculating changes and add up 
        Change = int(row[1])-Value
        Profits.append(Change)
        Value = int(row[1])

#the net total amount of "Profit/Losses" over the entire period
        Total_PL = Total_PL + int(row[1])

#The total number of months
        Total_Months += 1

#The greatest increase in profits (date and amount) over the entire period
    Greatest_Increase = max(Profits)
    Greatest_Index = Profits.index(Greatest_Increase)
    Greatest_Date = Dates[Greatest_Index]

#The greatest decrease in profits (date and amount) over the entire period
    Greatest_Decrease = min(Profits)
    Worst_index = Profits.index(Greatest_Decrease)
    Worst_Date = Dates[Worst_index]

#Average Change in Profits/Losses over the entire period
    Average_Change = sum(Profits)/len(Profits)

#print results as:
print('Financial Analysis')
print('_____________________')
print(f'Total Months: {str(Total_Months)}')
print(f"Total:${str(Total_PL)}")
print(f"Average Change: ${str(round(Average_Change,2))}")
print(f"Greatest Increase in Profits: {Greatest_Date} (${str(Greatest_Increase)})")
print(f"Greatest Decrease in Profits: {Worst_Date} (${str(Greatest_Decrease)})")

#exporting result to .txt file
Analysis = open("analysis.txt", "w")
line1 = "Financial Analysis"
line2 = "____________________"
line3 = str(f"Total Months: {str(Total_Months)}")
line4 = str(f"Total: ${str(Total_PL)}")
line5 = str(f"Average Change: ${str(round(Average_Change,2))}")
line6 = str(f"Greatest Increase in Profits: {Greatest_Date} (${str(Greatest_Increase)})")
line7 = str(f"Greatest Decrease in Profits: {Worst_Date} (${str(Greatest_Decrease)})")
Analysis.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,line5,line6,line7))












