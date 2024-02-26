# Problem Set 7
# Find Factorial

'''
    Write a function that calculates the factorial of a given number.
'''

# Define a function
# Get input from the user
# Multiply input times itself
# Print the calculation

def find_factorial():
    factorial = 1
    num = int(input("Enter a number: "))

    for i in range(1, (num + 1)):
        factorial = factorial * i
    print(f"The factorial of {num} is {factorial}.")

find_factorial()
