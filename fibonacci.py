#!/usr/bin/env python3

# Fibonacci Sequence Exercise
# TODO: (Read detailed instructions in the Readme file)
# Prompt the user for the number of terms.
# Validate that the input is a positive integer.
# Use a for loop to print the Fibonacci sequence up to that many terms.

# Fibonacci Sequence Generator (Basic Version)

def get_positive_integer(prompt):
    user_input = input(prompt)

    # Repeat until a valid positive integer is entered
    while not user_input.isdigit() or int(user_input) <= 0:
        print("Please enter a number greater than 0.")
        user_input = input(prompt)

    return int(user_input)

def generate_fibonacci(x):
    fib_sequence = []
    a = 0
    b = 1

    for i in range(x):
        fib_sequence.append(a)
        temp = a + b
        a = b
        b = temp

    return fib_sequence

def main():
    print("Fibonacci Sequence Generator")
    num_terms = get_positive_integer("Enter the number of terms: ")

    print("\nFirst", num_terms, "terms of the Fibonacci sequence:")
    fibonacci = generate_fibonacci(num_terms)

    for num in fibonacci:
        print(num)

# Run the program
main()

