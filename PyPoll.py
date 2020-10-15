# The data we need to retrieve:
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

# import datetime class from datetime module
import datetime as dt 
# now() attribute on datetime class gives us present time
now = dt.datetime.now()
# print("The time right now is ", now)

import csv
import random
import os
# import numpy - no module named numpy


# assign a variable to load csv file
file_to_load = os.path.join("resources", "election_results.csv") 

# assign variable to write to csv
file_to_save = os.path.join("analysis", "election_analysis.txt")

# initialize a total vote counter
total_votes = 0

# candidate options
candidate_options = []
candidate_votes = {}

# winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

## open and read the file
with open(file_to_load) as election_data:

    # to-do: perform analysis
    # read the file object with the reader function
    file_reader = csv.reader(election_data)

    # read the header row in csv file
    headers = next(file_reader)
    
    # print each row in csv file
    for row in file_reader:
        # add to total vote count
        total_votes += 1
        # print candidate name from each row
        candidate_name = row[2]
        # if candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # add candidate name to candidate list
            candidate_options.append(candidate_name)
            # begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0
         # add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

# calculate vote percentage for each candidate
for candidate_name in candidate_votes:
    # retireve vote count of a candidate
    votes = (candidate_votes[candidate_name])
    # calculate percentage (with one decimal place)
    vote_percentage = (float(votes) / float(total_votes))*100
    # print candidate, vote count and percentage
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")  

    # determine if the votes are greater than the winning count
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        # if true then set winning_count = votes and winning_percent = vote_percentage
        winning_count = votes
        winning_percentage = vote_percentage
        winning_percentage = vote_percentage
        # set winning_candidate = candidate's name
        winning_candidate = candidate_name
        winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
        
print(winning_candidate_summary)
