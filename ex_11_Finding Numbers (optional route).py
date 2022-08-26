import re
print(sum([int(x) for x in re.findall('([0-9]+)', open('regex_sum_1562112.txt').read())]))

# entire string
# print(open('regex_sum_1562112.txt').read())

# list of numbers (in str type) of the string that was read
# print(re.findall('([0-9]+)', open('regex_sum_1562112.txt').read()))