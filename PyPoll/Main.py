# Imports
import os
import csv


election_path = os.path.join('./Resources/election_data.csv')

# Path for output text file
output = os.path.join('./Analysis/output.txt')

# Initial variable
candidates ={}
total_votes=0

# Open & read CSV file
with open(election_path) as election:
    e_reader = csv.reader(election, delimiter=',')
    csv_header = next(e_reader)
# Calculate totals

    for row in e_reader:
        voter_ID = row[0]
        county = row[1]
        candidate = row[2]

        total_votes = total_votes + 1
        if candidate in candidates:
            votes = candidates[candidate] + 1
            candidate_update = {candidate: votes}
            candidates.update(candidate_update)
        else:
            candidates.update({candidate: 1})
# Output textfile
write_file = open(output, 'w')
print("Election Results")
print("----------------------------")
write_file.write(f"Election Results\n")
write_file.write(f"----------------------------\n")
print(f"Total Votes: {total_votes}")
print("----------------------------")
write_file.write(f"Total Votes: {total_votes}\n")
write_file.write(f"----------------------------\n")

# Loop again to find and output winner
most_votes = 0

for candidate, votes in candidates.items():
    percentage = "{:.3f}".format(votes / total_votes * 100)
    if votes > most_votes:
        most_votes = votes
        winner = candidate

    
    print(f"{candidate}: {percentage}% ({votes})")

    write_file.write(f"{candidate}: {percentage}% ({votes})\n")

print("----------------------------")
print(f"Winning Candidate: {winner}")
print("----------------------------")

write_file.write(f"----------------------------\n")
write_file.write(f"Winning Candidate: {winner}\n")
write_file.write(f"----------------------------\n")

write_file.close()