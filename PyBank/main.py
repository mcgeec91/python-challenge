# import
import csv


data_csv = "Resources/budget_data.csv"
output = "Resources/budget_analysis.txt"

# Variables
total_months = 0
total_revenue = 0

past_revenue = 0
rev_change = 0
greatest_increase = ["", 0]
greatest_decrease = ["", 999999999999999]

rev_changes = []

# open_data
with open(data_csv) as revenue_data:
    reader = csv.DictReader(revenue_data)

    # Loop through all the rows of data we collect
    for row in reader:

        # Calculate the total rev
        total_months = total_months + 1
        total_revenue = total_revenue + int(row["Profit/Losses"])

        # Keep track of changes
        rev_change = int(row["Profit/Losses"]) - past_revenue
       

        # Reset the value of past_revenue to the row I completed my analysis
        past_revenue = int(row["Profit/Losses"])
        # print(past_revenue)

        # Determine the greatest increase
        if (rev_change > greatest_increase[1]):
            greatest_increase[1] = rev_change
            greatest_increase[0] = row["Date"]

        if (rev_change < greatest_decrease[1]):
            greatest_decrease[1] = rev_change
            greatest_decrease[0] = row["Date"]

        # Add to the rev_changes list
        rev_changes.append(int(row["Profit/Losses"]))

    #average
    revenue_avg = sum(rev_changes) / len(rev_changes)
    

    print()
    print()
    print()
    print("Financial Analysis")
    print("-------------------------")
    print("Total Months: " + str(total_months))
    print("Total Revenue: " + "$" + str(total_revenue))
    print("Average Change: " + "$" + str(round(sum(rev_changes) / len(rev_changes),2)))
    print("Greatest Increase: " + str(greatest_increase[0]) + " ($" +  str(greatest_increase[1]) + ")") 
    print("Greatest Decrease: " + str(greatest_decrease[0]) + " ($" +  str(greatest_decrease[1]) + ")")
    


# Output
with open(output, "w") as txt_file:
    txt_file.write("Total Months: " + str(total_months))
    txt_file.write("\n")
    txt_file.write("Total Revenue: " + "$" + str(total_revenue))
    txt_file.write("\n")
    txt_file.write("Average Change: " + "$" + str(round(sum(rev_changes) / len(rev_changes),2)))
    txt_file.write("\n")
    txt_file.write("Greatest Increase: " + str(greatest_increase[0]) + " ($" + str(greatest_increase[1]) + ")") 
    txt_file.write("\n")
    txt_file.write("Greatest Decrease: " + str(greatest_decrease[0]) + " ($" + str(greatest_decrease[1]) + ")")