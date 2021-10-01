import csv
import os

file_to_load = os.path.join('Resources', 'election_results.csv')
file_to_save = os.path.join('Analysis', 'election_analysis.txt')
total_votes = 0
candidate_options = []
candidate_votes = {}
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

with open(file_to_load) as election_data:
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

# Print the header row.
    headers = next(file_reader)
    #print(headers)

 # Print each row in the CSV file.
    for row in file_reader:
          # Add to the total vote count.
          total_votes += 1
        
          # Print the candidate name from each row
          candidate_name = row[2]
        
          if candidate_name not in candidate_options:
               candidate_options.append(candidate_name)
                # Begin tracking that candidate's vote count.
               candidate_votes[candidate_name] = 0
          
          candidate_votes[candidate_name] += 1         

with open (file_to_save,"w") as txt_file:
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)

    for candidate_name in candidate_votes:
        # Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        # Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        # Print the candidate name and percentage of votes.
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results,end='')
        #with open (file_to_save,"w") as txt_file:
        txt_file.write(candidate_results)

        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # 2. If true then set winning_count = votes and winning_percent =
             # vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            # 3. Set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")

    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)


   