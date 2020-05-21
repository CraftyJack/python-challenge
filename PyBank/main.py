# PyBank homework assignment
# First, import os and csv
import os
import csv

# declare some variables
vMonths = 0
vPL = None
vDeltaPL = 0
vDeltaTotal = 0
vDeltaPLMax = ["MaxMon", 0]
vDeltaPLMin = ["MinMon", 0]
vTotalPL = 0

# set the path for the budget_data.csv file
budget_csv = os.path.join("Resources", "budget_data.csv")
# open up the budget_data.csv spreadsheet
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # this csv has a header row. 
    # Read the header row first
    csv_header = next(csvfile)
    # print it out to prove we found the right file.
    print(f"Header: {csv_header}")
# this csv has two columns.
# the first column is the month (MMM-YYYY).
# the second column is the profit/loss for that month.
    for row in csvreader:
        vMonths = vMonths + 1
        vTotalPL = vTotalPL + int(row[1])
        if vPL is not None:
            vDeltaPL = int(row[1]) - vPL
            vPL = int(row[1])
            vDeltaTotal = vDeltaTotal + vDeltaPL
            if vDeltaPL > vDeltaPLMax[1]:
                vDeltaPLMax[0] = row[0]
                vDeltaPLMax[1] = vDeltaPL
            elif vDeltaPL < vDeltaPLMin[1]:
                vDeltaPLMin[0] = row[0]
                vDeltaPLMin[1] = vDeltaPL
        else:
            vPL = int(row[1])


print(f"Financial Analysis")
print(f"----------------------------")
print(f"Total Months: {vMonths}")
print(f"Total: ${vTotalPL}")
print(f"Average  Change: ${round(vDeltaTotal / (vMonths -1),2)}")
print(f"Greatest Increase in Profits: {vDeltaPLMax[0]} (${vDeltaPLMax[1]})")
print(f"Greatest Decrease in Profits: {vDeltaPLMin[0]} (${vDeltaPLMin[1]})")

# we want to know:

#   * The total number of months included in the dataset
# I am assuming each row is one month.

#   * The net total amount of "Profit/Losses" over the entire period
# This is calculated by adding together all of the values from column 2

#   * The average of the changes in "Profit/Losses" over the entire period
# This is the average of row n - row (n-1)

#   * The greatest increase in profits (date and amount) over the entire period
# This is the maximum value for row n - row (n-1)

#   * The greatest decrease in losses (date and amount) over the entire period
# This is the minimum value for row n - row (n-1)