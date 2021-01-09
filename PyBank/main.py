import os
import csv

#csv path

csvpath = os.path.join('Resources' , 'budget_data.csv')

# variables 
changes =[]
count_date = []

months_total = 0
revenue_total =0

greatest_increase = 0
greatest_increase_month = 0
greatest_decrease = 0
greatest_decrease_month = 0

# Opening CSV
with open(csvpath, newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    next(csvreader, None)
    row = next(csvreader)

# calculating the revenue and months
    profit_past = int(row[1])
    months_total = months_total + 1
    revenue_total = revenue_total + int(row[1])
    greatest_increase = int(row[1])
    greatest_increase_month = row[0]

    for row in csvreader:
 
        months_total = months_total+ 1
        revenue_total = revenue_total + int(row[1])

        # Calculating change
        change = int(row[1]) - profit_past
        changes.append(change)
        profit_past = int(row[1])
        count_date.append(row[0])
        
        # greatest increase
        if int(row[1]) > greatest_increase:
            greatest_increase = int(row[1])
            greatest_increase_month = row[0]
            
        # greatest decrease
        if int(row[1]) < greatest_decrease:
            greatest_decrease = int(row[1])
            greatest_decrease_month = row[0]  
      
    #  average and date
    average_change = sum(changes)/len(changes)

    high = max(changes)
    low = min(changes)


    print("Financial Analysis")
    print("---------------------------------------------------------")
    print("Total Months  : " + str(months_total))
    print("Total Amount  : $" + str(revenue_total))
    print("Average Change: $" + str(average_change))
    print("Greatest Increase in Profits :  " + greatest_increase_month, "(",max(changes),")")
    print("Greatest Decrease in Profits :  " + greatest_decrease_month, "(",min(changes),")")

# output txt
with open('output.txt', 'w') as outtxt:

   # f = open("output.txt", "w")
    outtxt.write("Financial Analysis\n")
    outtxt.write("----------------------------\n")        
    outtxt.write("Total Months  : " + str(months_total) + "\n")
    outtxt.write("Total Amount  : $" + str(revenue_total)+ "\n")
    outtxt.write("Average Change: $" + str(format(average_change, '.2f')) + "\n")
    outtxt.write("Greatest Increase in Profits :  " + greatest_increase_month 
      + " ($" + str( max(changes) )+ ")" + ")\n")
    outtxt.write("Greatest Decrease in Profits :  " + greatest_decrease_month 
      + " ($" + str(min(changes)) + ")" + "\n")
    outtxt.close()   
        