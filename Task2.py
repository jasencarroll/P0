"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

phone_numbers = []

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

num_durations = []

for call in calls:
    for num in nums:
        if call[0] == num:
            num_durations.append([num, call[3]])
        elif call[1] == num:
            num_durations.append([num, call[3]])

nums_dict = dict.fromkeys(nums)
for nums in nums_dict:
    nums_dict[nums] = 0

for calls in num_durations:
    for key in nums_dict:
        if calls[0] == key:
            nums_dict[key] = nums_dict[key] + int(calls[1])

# Get the number [0] associated with the greaters value in [1]

print(len(nums_dict))
print(max(nums_dict.values()))

print(list(nums_dict.keys())[list(nums_dict.values()).index(max(nums_dict.values()))], "spent the longest time", max(nums_dict.values()), "seconds, on the phone during September 2016.")