import os
import numpy as np

def clear_terminal():
    # Clear the terminal screen in Windows
    _ = os.system('cls')

# Now you can call clear_terminal() whenever you want to clear the terminal screen
clear_terminal()

# Define the range within which you want to generate random numbers
start_range = 10000
end_range = 100000  # Adjust the end range as per your requirement

# Generate 5000 unique random numbers within the specified range
random_numbers = np.random.choice(range(start_range, end_range + 1), size=5000, replace=False)

# Sort the random numbers in ascending order
random_numbers_sorted = np.sort(random_numbers)

# Convert the numbers to a string with each number on a new line
numbers_string = '\n'.join(map(str, random_numbers_sorted))

# Write the numbers to a text file
with open('random_numbers.txt', 'w') as file:
    file.write(numbers_string)
print("Random numbers have been saved to 'random_numbers.txt'.")
