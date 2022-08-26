import re

fh = open('regex_sum_1562112.txt')

num_list = []

for ln in fh:
    ln = ln.rstrip()
    ln_list = (re.findall('([0-9]+)', ln))
    ln_list_length = len(ln_list)

    if ln_list_length > 0:
        for i in ln_list:
            num_list.append(int(i))
            # print(i)

# print(num_list)
print(f'Sum: {int(sum(num_list))}')