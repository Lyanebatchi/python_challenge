# Import os module
import os

#Import CSV module
import csv

# Specify the paths for the CSV files
budget_data_csv = os.path.join('Resources', 'budget_data.csv')


# Create a function that computes the total net amount of profit or losses throughout a given time span
def calculate_net_total(file_path):
    # Define  variables
    net_total = 0
    total_months = 0
    previous_profit_loss = 0
    monthly_change = []
    increase= ["", 0]
    decrease = ["", 0]
    #Read the CSV file
    with open(file_path,'r') as csvfile:
        #Create a CSV reader object 
        csvreader = csv.reader(csvfile)
        #Skip the header row
        next(csvreader)
        first_row = next(csvreader)
        total_months += 1
        net_total += int(first_row[1])
        previous_profit_loss = int(first_row[1])
        
        # Go through each individual in the CSV file
        for row in csvreader:
            #Extract the relevant data from the row
            date = row[0]
            profit_loss = int(row[1])

            #Update the total months
            total_months += 1

            #Update the net total amount of profit or losses
            net_total += profit_loss

            #Calculate the average in profit or lossesover the entire period 
            net_change = profit_loss - previous_profit_loss
            monthly_change.append(net_change)
            #average_change = (net_total - previous_profit_loss)/ total_months

            #update the previous profit or loss for the next iteration
            previous_profit_loss = profit_loss
            
            if net_change > increase[1]:
                increase[1] = net_change
                increase[0] = date

            
            if net_change < decrease[1]:
                decrease[1] = net_change
                decrease[0] = date

    average_change = sum(monthly_change ) / len(monthly_change)
    #Return the calculated values
            # return total_months, net_total, average_change
    output_file = os.path.join("analysis", "budget_analysis.txt")
    with open (output_file,"w") as file:
        output = (f"Financial Analysis\n"
                f"-----------------------------\n"
                f"Total Months: {total_months}\n"
                f"Total: ${net_total}\n"
                f"Average change: ${average_change}\n"
                f"Greatest Increase in Profits: {increase[0]} (${increase[1]})\n"
                f"Greatest Decrease in Profits: {decrease[0]} (${decrease[1]})\n")
        print(output)
        file.write(output)
#Call the function to calculate the net total amount of profit over a certain period of time
calculate_net_total(budget_data_csv)


# Print the analysis results to the terminal
# print("Financial Analysis ")
# print ("-----------------------------")
# print(f"Total Months: {total_months}")
# print(f"Total: ${net_total}")
# print(f"Average change: ${average_change}")




