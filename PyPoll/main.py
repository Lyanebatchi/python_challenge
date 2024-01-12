# Import os module
import os

#Import CSV module
import csv

# Specify the paths for the CSV files
election_data = os.path.join('Resources','election_data.csv')
#Define a function to analyze the election data and find the winner
# def analyze_election_data(file_path):
#Define variables
winner = ""
winner_vote = 0
total_votes = 0
candidate_votes = {}
candidate_name = []

#Open the CSV file
with open(election_data, 'r') as csvfile:
    #Create a CSV reader object
    csvreader = csv.reader(csvfile)

    #Skip the header row
    next(csvreader)

    # Go through each row in the CSV file
    for row in csvreader:
        #Extract the relevant data from the row
        candidate = row[2]
        

        #Update the total number of votes
        total_votes += 1

        #Update the total number votes for candidate
        if candidate not in candidate_name:
            candidate_name.append(candidate)
        
            candidate_votes[candidate] = 0
        candidate_votes[candidate] += 1
            #Check if candidate has won the election
            # if votes > candidate_votes[winner]:
            #     winner = candidate
#Call the function to analyze the election data and find winner
# total_votes, candidate_votes, winner = analyze_election_data(election_data_csv)
output_file = os.path.join("analysis", "election_analysis.txt")
with open(output_file, "w") as file:
    election_result = (
        "Election Results\n"
        "------------------------\n"
        f"Total Votes: {total_votes}\n")
    print(election_result)
    file.write(election_result)

    for candidate, votes in candidate_votes.items():
        candidate_result = (f"{candidate}: {((votes / total_votes) * 100):.3f}% ({votes})\n")
        print(candidate_result)
        file.write(candidate_result)
        if votes > winner_vote:
            winner_vote = votes
            winner = candidate
    winner_result = (
        "---------------------------\n"
        f"winner: {winner}\n"
        "-----------------------------\n")
    print(winner_result) 
    file.write(winner_result)
