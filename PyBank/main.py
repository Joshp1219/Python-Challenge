import os
import csv
csvpath = os.path.join('Resources','budget_data.csv')

Months = []
Monthly_Total = []
Monthly_Changes = []


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_Header = next(csvfile)
    
    for row in csvreader:
        Months.append(row[0])
        Monthly_Total.append(int(row[1]))
    for i in range(len(Monthly_Total)-1):
        Monthly_Changes.append(int(Monthly_Total[i+1])-int(Monthly_Total[i]))

Greatest_Inc_Month = Monthly_Changes.index(max(Monthly_Changes))+1
Greatest_Dec_Month = Monthly_Changes.index(min(Monthly_Changes))+1

Greatest_Inc_Value = max(Monthly_Changes)
Greatest_Dec_Value = min(Monthly_Changes)

print("Financial Analysis")
print("--------------------------------------")
print(f"Total Months: {len(Months)}") 
print(f"Total: {sum(Monthly_Total)}") 
print(f"Average Change: {round(sum(Monthly_Changes)/len(Monthly_Changes),2)}") 
print(f"Greatest Increase in Profits: {Months[Greatest_Inc_Month]} ${str(Greatest_Inc_Value)}") 
print(f"Greatest Decrease in Profits: {Months[Greatest_Dec_Month]} ${str(Greatest_Dec_Value)}") 

output_file = os.path.join('Analysis', 'analysis.txt')
with open(output_file, "w") as txtfile:
    txtfile.write("Financial Analysis" + "\n")
    txtfile.write("--------------------------------------"  + "\n")
    txtfile.write(f"Total Months: {len(Months)}"  + "\n") 
    txtfile.write(f"Total: {sum(Monthly_Total)}"  + "\n") 
    txtfile.write(f"Average Change: {round(sum(Monthly_Changes)/len(Monthly_Changes),2)}"  + "\n") 
    txtfile.write(f"Greatest Increase in Profits: {Months[Greatest_Inc_Month]} ${str(Greatest_Inc_Value)}"  + "\n") 
    txtfile.write(f"Greatest Decrease in Profits: {Months[Greatest_Dec_Month]} ${str(Greatest_Dec_Value)}"  + "\n")
    txtfile.write("--------------------------------------" + "\n")
    