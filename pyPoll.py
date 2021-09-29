# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 6. The winner of the election based on popular vote

import csv
import os

file_to_load = os.path.join('Resources', 'election_results.csv')
file_to_save = os.path.join('Analysis', 'election_analysis.txt')

with open(file_to_load) as election_data:
# Read the file object with the reader function.
    file_reader = csv.reader(election_data)

# Print the header row.
    headers = next(file_reader)
    print(headers)

# Print each row in the CSV file.
#    for row in file_reader:
#        print(row)

#with open(file_to_save,"w") as outfile:
#     outfile.write("Arapahoe, ")
#     outfile.write("Denver, ")
#     outfile.write("Jefferson\n")
#     outfile.write("10101010")
   