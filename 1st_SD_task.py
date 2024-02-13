import bisect
import time
import osdfgdfg

def clear_terminal():
    # Clear the terminal screen in Windows
    _ = os.system('cls')

# Now you can call clear_terminal() whenever you want to clear the terminal screen
clear_terminal()
'''
# Create a set of the numbers in the file for faster lookup
numbers_set = set(numbers_in_file)
# Check for a number that does not belong to the file
for number in range(start_range, end_range + 1):
    if number not in numbers_set:
        print("Number", number, "does not belong to the file.")
        break
'''
# Prompt the user to input a number
numb = int(input("Please enter a number: "))
# Display the entered number
print("You entered:", numb)

start = time.time_ns()
def main(numb): 
    # Read the numbers from the text file
    with open('random_numbers.txt', 'r') as file:
        numbers_in_file = [int(line.strip()) for line in file]
    # Convert numbers_set to a sorted list
    sorted_numbers_list = sorted(numbers_in_file)
    # Find the index where the numb would be inserted to maintain sorted order
    index_to_insert = bisect.bisect(sorted_numbers_list, numb)
    # Numbers between which the number_to_find is located
    number_before = sorted_numbers_list[index_to_insert - 1]
    number_after = sorted_numbers_list[index_to_insert]
    print("The number", numb, "is located between", number_before, "and", number_after)
main(numb)
duration_ns = time.time_ns() - start

duration_ms = duration_ns / 1_000_000
print(duration_ms, "ms")
