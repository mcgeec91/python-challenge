# Dependencies
import csv

#incoming/outgoing
election_csv = "Resources/election_data.csv"
file_to_output = "Resources/election_analysis.txt"

#variables
vote = 0
winner_vote = 0
total = 0
greatest_votes = ["", 0]
candidates = []
candidate_vote_count = {}

#csv.DictReader
with open(election_csv) as election_data:
    reader = csv.DictReader(election_data)

    for row in reader:
        vote = vote + 1
        total = row["Candidate"]        

        if row["Candidate"] not in candidates:
            
            candidates.append(row["Candidate"])

            candidate_vote_count[row["Candidate"]] = 1
            
        else:
            candidate_vote_count[row["Candidate"]] = candidate_vote_count[row["Candidate"]] + 1
		
		
#The total number of months included in the dataset


#The total number of votes cast

#A complete list of candidates who received votes

#The percentage of votes each candidate won

#The total number of votes each candidate won

#The winner of the election based on popular vote.


    print()
    print()
    print()
    print("Election Results")
    print("-------------------------")
    print("Total Votes " + str(vote))
    print("-------------------------")
#results
    for candidate in candidate_vote_count:
        print(candidate + " " + str(round(((candidate_vote_count[candidate]/vote)*100))) + "%" + " (" + str(candidate_vote_count[candidate]) + ")") 
        candidates = (candidate + " " + str(round(((candidate_vote_count[candidate]/vote)*100))) + "%" + " (" + str(candidate_vote_count[candidate]) + ")") 
		
		
# Output Files
with open(file_to_output, "w") as txt_file:
    
    txt_file.write("Election Results")
    txt_file.write("\n")
    txt_file.write("-------------------------")
    txt_file.write("\n")
    txt_file.write(str(winner))
    txt_file.write("\n")
    txt_file.write("-------------------------")
    txt_file.write("\n")
    txt_file.write("Winner: " + str(winner[0]))
    txt_file.write("\n")
    txt_file.write("Total Votes " + str(votes))