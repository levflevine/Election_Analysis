# Election Audit Project

## Project Overview
Seth and Tom from the Colorado Board of Elections have requested to support the election audit of a recent local congressional election. The audit included the following steps:
1. Calculate the total number of votest cast
2. Get a complete list of candidates, who received votes
3. Calculate the total number of votes each candidate received
4. Calculate the percentage of votes each candidate won
5. Determine the winner of the election based on popular vote.

After completing the initial audit, the election commission has requested the following additional data to complete the audit:
1. The voter turnout for each county
2. The percentage of votes from each county out of the total count
3. The county with the highest turnout

The audit results needed to be demonstrated in the *Terminal* and in the *Text File*

## Resources
- Data Source: [election_results.csv](https://2u-data-curriculum-team.s3.amazonaws.com/dataviz-online/module_3/election_results.csv)
- Software: Python 3.7.6, Visual Studio Code 1.60.2

## Audit Results
The analysis of the election confirmed that
- There were **369,711** votes cast in the election
- The votes cast breakdown by county in the precinct is the following. 
  - ***Jefferson***: **38,855** votes, which represented **10.5%** of the total votes cast
  - ***Denver***: **306,055** votes, which represented **82.8%** of the total votes cast
  - ***Arapahoe***: **24,801** votes, which represented **6.7%** of the total votes cast.
- **Denver county** had the largest number of votes: *306,055*.
- The candidates were:
  - ***Charles Casper Stockham***
  - ***Diana DeGette***
  - ***Raymon Anthony Doane***
- The Candidate results were:
  - ***Charles Casper Stockham*** received **23.0%** of the vote and **85,213** number of votes
  - ***Diana DeGette*** received **73.8%** of the vote and **272,892** number of votes
  - ***Raymon Anthony Doane*** received **3.1%** of the vote and **11,606** number of votes
 - The **winner of the election** was:
   - ***Diana DeGette***, who received 73.8% of the vote and 272,892 number of votes.
   
### The audit results shown in the Terminal 
![Terminal Screenshot](/Resources/Terminal_Screen.png)

### The audit results shown in the Election_Results.txt lile
![Terminal Screenshot](/Resources/Election_Results_Screen.png)

## Election-Audit Summary
The project has resulted in the development of a digital application (Application) that can be used by the State of Colorado in future elections to improve the efficiency, timeliness, and accuracy of election result audits. 

It is proposed that the Application be further enhanced with the following product features that will drive incremental value for State future audits, as follows.
1. Script that will **rearrange the ballot results in the ascending order of County Name and Candidate Name data fields** to group together the results by County and by Candidate in the election_results.csv file.
2. Enable **an input form for a user to specify a folder name for the election results data input and a folder name for the audit analysis data output** based on the user preferences instead of the hard-coded "Resources" and "Analysis" folders.
3. Develop **a (graphical) user interface** to simplify the data entry and visualize the audit results reporting.

