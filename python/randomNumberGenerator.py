import sys
import random
from random import randint  # Import randint from the standard library random module

# Generate 2000 random numbers between 1 and 5000
numbers = [random.randint(1, 5000) for _ in range(2000)]

# Save the numbers to a file (replace "unsorted_numbers.txt" with your desired filename)
with open("unsorted_numbers.txt", "w") as file:
    for number in numbers:
        file.write(str(number) + "\n")

print("2000 random numbers generated and saved to unsorted_numbers.txt")