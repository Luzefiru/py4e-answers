import re

inp = input('Enter a regular expression: ')
fh = open('mbox.txt')

count = 0
for ln in fh:
    if re.search(inp, ln):
        count += 1

print(f'mbox.txt had {count} lines that matched {inp}')