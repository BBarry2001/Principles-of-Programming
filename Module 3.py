# Part 1: Calculating the Total Meal Cost with Tip and Tax

# Input: Ask the user to enter the cost of the meal
meal_cost = float(input("Enter the cost of your meal: $"))

# Process: Calculate tip and tax amounts
tip_amount = meal_cost * 0.18  # 18% tip
tax_amount = meal_cost * 0.07  # 7% tax
total_cost = meal_cost + tip_amount + tax_amount  # Total amount

# Output: Display tip, tax, and total amounts
print(f"Tip amount: ${tip_amount:.2f}")
print(f"Tax amount: ${tax_amount:.2f}")
print(f"Total cost of the meal: ${total_cost:.2f}")


# Part 2: Calculating Alarm Time on a 24-Hour Clock

# Input: Ask the user for the current time and wait hours
current_time = int(input("Enter the current time (0-23): "))
wait_hours = int(input("Enter the number of hours to wait: "))

# Process: Calculate the time when the alarm will go off
alarm_time = (current_time + wait_hours) % 24

# Output: Display the alarm time
print(f"The alarm will go off at: {alarm_time}:00")
