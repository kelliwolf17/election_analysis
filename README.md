# Election Analysis
# Contents 
Python file with final code

Text file with final results

CSV file with raw data

# Overview of Election Audit
The purpose of this election audit analysis was to determine the total votes cast, how many votes per candidate, the percentage of votes per candidate, how many votes per county, and the percentage of votes per county. Typically this audit is done in Excel, but we were given an opportunity to prove it can be done with Python to simplify the process for future elections.

# Election Audit Results
Please see the below list for a summary of the results of the election:
  - Total votes
  
    ![total_votes](https://user-images.githubusercontent.com/71397190/96388028-d94ff180-116b-11eb-83d6-867fa9769c03.PNG)
    
  - Vote Breakdown by county
  
    ![county_votes](https://user-images.githubusercontent.com/71397190/96388032-dfde6900-116b-11eb-9e8b-d0778a469c93.PNG)
    
  - Denver County had the largest number of votes
  
    ![county_winner](https://user-images.githubusercontent.com/71397190/96388034-e240c300-116b-11eb-923d-a0ab777a3a6d.PNG)
    
  - Breakdown of votes by candidate
  
    ![candidates](https://user-images.githubusercontent.com/71397190/96388031-de14a580-116b-11eb-8403-cf0f85dfec81.PNG)
    
  - Election winner
  
    ![candidate_winner](https://user-images.githubusercontent.com/71397190/96388030-dc4ae200-116b-11eb-955c-e5cca0d8b1ff.PNG)
  
# Election Audit Summary
This code can easily be used for any other election held to help determine the same metrics. So long as the CSV file formatting remains the same, the only line of code that would need to be changed is Line 9 when you load the CSV file (file_to_load = os.path.join("resources", "election_results.csv")). The file would be changed to the new file name of the new data. You could also change the name of the text file in Line 11 if you wish, otherwise the folder structure would also need to remain the same (i.e. maintaining a "resources" and "analysis" folder). If the data was for a larger election population, like for an entire state or for the country, then more repetition statements could be written to gather new metrics. This would be quite simple as there are two repetition statements already in the code, for the candidate and county breakdown results, to model any new repetition statement after. 
  
    
