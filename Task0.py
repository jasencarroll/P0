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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

first_text = texts[0]
FTIN = first_text[0]
FTAN = first_text[1]
FTT = first_text[2]

last_call = calls[-1]
LCIN = last_call[0]
LCAN = last_call[1]
LCT = last_call[2]
LCTD = last_call[3]

print(f"First record of texts, {FTIN} texts {FTAN} at time {FTT}")
print(f"Last record of calls, {LCIN} calls {LCAN} at time {LCT}, lasting {LCTD} seconds.")
