"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

phone_numbers = []

# Get all of the numbers from the text log.
for text in texts:
    phone_numbers.append(text[0])
    phone_numbers.append(text[1])

# Get all of the numbers from the call log.
for call in calls:
    phone_numbers.append(call[0])
    phone_numbers.append(call[1])

# Initialize a new list
nums = []

# Using list comprehension:
# - Append the phone number (x)
# - For every phone number in the original list
# - If it hasn't already been appended
for number in phone_numbers:
    if number not in nums:
        nums.append(number)

count = len(nums)
print(f"There are {count} different telephone numbers in the records.")
