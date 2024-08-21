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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""


## Make Outgoing 
incoming = []
outgoing = []

for call in calls:
    outgoing.append(call[0])
    incoming.append(call[1])

all_calls = incoming + outgoing

all_texts = []
for text in texts:
    all_texts.append(text[0])
    all_texts.append(text[1])

telemarketers = []

for call in all_calls:
    if call not in incoming:
        if call in outgoing:
            if call not in all_texts:
                if call not in telemarketers:
                    telemarketers.append(call)

## Never send text or receive text
# use what you did in task 1

## Never receive call

#incoming

# Print Line
telemarketers.sort()
print(f"These numbers could be telemarketers: ")
for num in telemarketers:
    print(num)
