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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

# Part A - all area codes/prefixes called by people in Bangalore.

## Calls from (080)

bangalore_callers = []
for call in calls:
    if call[0].startswith('(080)'):
        bangalore_callers.append(call)


## Fixed Lines

#refactor with .startswith
bang_out = []
for call in bangalore_callers:
    if '(' in call[1]:
        bang_out.append(call[1])

## Mobiles

# have a space in the middle and always starts with 7, 8, or 9.
mobiles = []

for call in bangalore_callers:
    if ' ' in call[1]:
        if call[1].startswith('7') or call[1].startswith('8') or call[1].startswith('9'):
          bang_out.append(call[1])


## Telemarketers - 140
telemarketers = []

for call in bangalore_callers:
    if call[1].startswith('140'):
        bang_out.append(call[1])

#print(bang_out)
# Now I need a list of all of the area codes.

# if it starts with a parenthesis, find the other one and strip everything after.
area_code_list = []
for call in bang_out:
    if '(' in call:
        area_code_end = call.find(')')
        area_code = call[1:area_code_end]
        if area_code not in area_code_list:
            area_code_list.append(area_code)

# if it starts with a 140 strip everything else
area_code_list.append('140')

# if it starts with a 7, 8, or 9, strip everything starting at the space. 
for call in bang_out:
    if ' ' in call:
        if call.startswith('7') or call.startswith('8') or call.startswith('9'):
              area_code_end = 4
              area_code = call[0:area_code_end]    
              if area_code not in area_code_list:
                  area_code_list.append(area_code)

# Sort the list as requested
area_code_list.sort()

# Print the answer as part of a message:
#print(f"The numbers called by people in Bangalore have codes: ")
#for area_code in area_code_list:
#    print(area_code)

# Part B - what % are fixed to fixed?

## (080) to (080)
area_code_dict = dict.fromkeys(area_code_list)
for area_codes in area_code_dict:
    area_code_dict[area_codes] = 0

for call in bang_out:
    for key in area_code_dict:
        if str(key) in call:
            area_code_dict[key] = area_code_dict[key] + int(1)

print(area_code_dict)

total_calls = 0
for call in bang_out:
    total_calls = total_calls + 1

percent080 = float((area_code_dict['080'] / total_calls)*100).__round__(2)

    

# Print the answer as a part of a message::
print(f"{percent080} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")
