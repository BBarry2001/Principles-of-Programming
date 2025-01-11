# Part 2: Multiplication and Division of Two Numbers

# Input: Ask the user for two numbers
num1 = float(input("Enter the first number (num1): "))
num2 = float(input("Enter the second number (num2): "))

# Process: Perform multiplication
multiplication_result = num1 * num2

# Process: Perform division, checking for division by zero
if num2 != 0:
    division_result = num1 / num2
    # Output: Display the results of multiplication and division
    print(f"The result of multiplying {num1} and {num2} is: {multiplication_result}")
    print(f"The result of dividing {num1} by {num2} is: {division_result}")
else:
    # Output: Handle division by zero error
    print(f"Cannot divide by zero. The multiplication result is: {multiplication_result}")
