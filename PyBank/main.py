# Import Dependencies
import pandas as pd

#Load the Budget_data.csv into a dataframe
df = pd.read_csv("Resources/budget_data.csv")

# Count the number of Months in the DataFrame. Each row under data is a separate month.
total_months = len(df)

# Calculate the net total amount of "Profit/Losses" over the entire period
net_total = df["Profit/Losses"].sum()

# Calculate the changes in "Profit/Losses" by taking the difference between each row
df["Profit Change"] = df["Profit/Losses"].diff()

# Calculate the average change
average_change = df["Profit Change"].mean()

# Calculate the Greatest Increase and Decrease in Profits
    
    #The greatest increase in profits over the entire period
max_increase_row = df[df["Profit Change"] == df["Profit Change"].max()]

    #The greatest decrease in profits over the entire period
max_decrease_row = df[df["Profit Change"] == df["Profit Change"].min()]

# The date and corresponding greatest increase/decrease values.
greatest_increase_date = max_increase_row["Date"].values[0]
greatest_increase_amount = max_increase_row["Profit Change"].values[0]
greatest_decrease_date = max_decrease_row["Date"].values[0]
greatest_decrease_amount = max_decrease_row["Profit Change"].values[0]

#Print all of the results
print("Financial Analysis")
print("---------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total:.2f}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase_amount:.2f})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease_amount:.2f})")