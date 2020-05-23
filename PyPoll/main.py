# PyPoll homework assignment
# First, import os and csv
import os
import csv

# declare some variables
vTotalVotes = 0
dTally = {}

# The csv has three columns: Voter ID, County, and Candidate
# All three can be strings for our purposes.
# Need to find the following:
# The total number of votes cast
#   > This will be a count of the number of rows in the csv.
# A complete list of candidates who received votes
#   > This will be a list of the unique names that appear in the 'Candidate' column.
# The percentage of votes each candidate won
#   > This will be a count of the number of times each candidate's name appears, divided by total votes
# The total number of votes each candidate won
#   > This will be a count of the number of times each candidate's name appears.
# The winner of the election based on popular vote.
#   > This will be the name of the candidate that has the highest number of votes

# Start by setting the path, opening the file, and grabbing the header row.
# set the path for the budget_data.csv file
votes_csv = os.path.join("Resources", "election_data.csv")
with open(votes_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # this csv has a header row. 
    # Read the header row first
    csv_header = next(csvfile)

    # loop through the file
    for row in csvreader:
        # count up all the votes
        vTotalVotes = vTotalVotes + 1
        # build a dictionary of candidates and vote totals
        if row[2] in dTally:
            # if a candidate's name appears and we already have them in the dictionary, add 1 to their total
            dTally[row[2]] = dTally[row[2]] + 1
        else:
            # otherwise, add them to the dictionary
            dTally[row[2]] = 1
# now, it gets a little backwards
# Flip the dictionary so we can use the vote totals as a key to find the winner as a value
dTallyFlipped = [(value, key) for key, value in dTally.items()]
vWinner = max(dTallyFlipped)[1]
# print results to the terminal
print(f"Election Results")
print(f"-------------------------")
print(f"Total Votes: {vTotalVotes}")
print(f"-------------------------")
for i in dTally:
    print(f"{i}: {format(100*dTally[i]/vTotalVotes, '.3f')}% {dTally[i]}")
print(f"-------------------------")
print(f"Winner: {vWinner}")
print(f"-------------------------")
# print results to the output file
analysis_csv = os.path.join("analysis", "PyPoll_analysis.txt")
with open(analysis_csv, "w") as analysis_file:
    print(f"Election Results", file = analysis_file)
    print(f"-------------------------", file = analysis_file)
    print(f"Total Votes: {vTotalVotes}", file = analysis_file)
    print(f"-------------------------", file = analysis_file)
    for i in dTally:
        print(f"{i}: {format(100*dTally[i]/vTotalVotes, '.3f')}% {dTally[i]}", file = analysis_file)
    print(f"-------------------------", file = analysis_file)
    print(f"Winner: {vWinner}", file = analysis_file)
    print(f"-------------------------", file = analysis_file)