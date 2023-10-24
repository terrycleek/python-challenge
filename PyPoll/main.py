# Import Dependencies
import pandas as pd

# Load the election_data.csv into a DataFrame
df = pd.read_csv("Resources/election_data.csv")

# Calculate the total number of votes cast
total_votes = len(df)

# Complete a list of candidates who received votes
unique_candidates = df["Candidate"].unique()

#Calculat the total number of votes each candidate won
candidate_votes = df["Candidate"].value_counts().to_dict()

#Calculate the percentage of votes each candidate won (candidate/Total X 100)
percentage_votes = {candidate: (votes / total_votes) * 100 for candidate, votes in candidate_votes.items()}

# Check to see the Winner based on Popular Vote.
winner = max(candidate_votes, key=candidate_votes.get)

# Print Results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate in unique_candidates:
    print(f"{candidate}: {percentage_votes[candidate]:.3f}% ({candidate_votes[candidate]})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Save the results to a text file
with open("PyPoll.txt", "w") as f:
    # Write the results to the file
    f.write("Election Results\n")
    f.write("-------------------------\n")
    f.write(f"Total Votes: {total_votes}\n")
    f.write("-------------------------\n")
    
    for candidate in unique_candidates:
        f.write(f"{candidate}: {percentage_votes[candidate]:.3f}% ({candidate_votes[candidate]})\n")
    
    f.write("-------------------------\n")
    f.write(f"Winner: {winner}\n")
    f.write("-------------------------\n")

