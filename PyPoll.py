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

## open and read the file
with open(file_to_load) as election_data:

    # to-do: perform analysis
    # read the file object with the reader function
    file_reader = csv.reader(election_data)

    # print the header row in csv file
    headers = next(file_reader)
    print(headers)

# using open() function with the "w" mode to write data to the file
# txt_file = open(file_to_save, "w")

# practice writing data to election_analysis.txt
# txt_file.write("Counties in the Election\n--------------------------\nArapahoe\nDenver\nJefferson")


# close file
# txt_file.close()

# close the file - if opening file with open() then you don't need to close it
# election_data.close()
