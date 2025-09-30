#!/usr/bin/env python3

# Fibonacci Sequence Exercise
# TODO: (Read detailed instructions in the Readme file)
# Prompt the user for the number of terms.
# Validate that the input is a positive integer.
# Use a for loop to print the Fibonacci sequence up to that many terms.

def get_positive_integer(prompt="Enter the number of terms: "):
    while True:
        try:
            user_input = input(prompt)
            number = int(user_input)
            if number > 0:
                return number
            else:
                print("Please enter a number greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def generate_fibonacci(x):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(x):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

def main():
    print("Fibonacci Sequence Generator")
    num_terms = get_positive_integer()

    print(f"\nFirst {num_terms} terms of the Fibonacci sequence:")
    fibonacci = generate_fibonacci(num_terms)
    for num in fibonacci:
        print(num)

if __name__ == "__main__":
    main()
