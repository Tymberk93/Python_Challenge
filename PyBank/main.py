import os
import csv

budget_path = os.path.join('./Resources/budget_data.csv')

# Path for output text file
output = os.path.join('./Analysis/output.txt')

# open & read CSV file
with open(budget_path) as budget_file:
    budget_reader = csv.reader(budget_file, delimiter=',')
    csv_header = next(budget_reader)

    # Set variables = 0
    total_months = 0
    total_loss = 0
    increase = 0
    decrease = 0
    total_change = 0
    opening_loss = 0
    closing_loss = 0
    previous_row = ["",0]
    increase_decrease = 0
    
# Loop 

    for row in budget_reader:
            
        total_months = total_months + 1
        total_loss = total_loss + int(row[1])

        if opening_loss == 0:
            opening_loss = int(row[1])
        else:
            closing_loss = int(row[1])
                
            increase_decrease = int(row[1]) - int(previous_row[1])
                # Greatest increase in profits over the entire period
        if increase < increase_decrease:
            increase = increase_decrease
            greatest_i_month = str(row[0])

                # Greatest decrease in losses over the entire period
        if decrease > increase_decrease:
            decrease = increase_decrease
            greatest_d_month = str(row[0])

                # Reset row for next loop
        row_before = row

        # Average changes in Profit/Losses over the entire period
    average_changes = (closing_loss - opening_loss) / (total_months - 1)

# Average change
format_change = "{:.2f}".format(average_changes)

# Print data
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_loss}")
print(f"Average Change: ${format_change}")
print(f"Greatest Increase in Profits: {greatest_i_month} (${increase})")
print(f"Greatest Decrease in Profits: {greatest_d_month} (${decrease})")

# Print output data
write_file = open(output, 'w')
write_file.write(f"Financial Analysis\n")
write_file.write(f"----------------------------\n")
write_file.write(f"Total Months: {total_months}\n")
write_file.write(f"Total: ${total_loss}\n")
write_file.write(f"Average Change: ${format_change}\n")
write_file.write(f"Greatest Increase in Profits: {greatest_i_month} (${increase})\n")
write_file.write(f"Greatest Decrease in Profits: {greatest_d_month} (${decrease})\n")
write_file.close()