import re

fh = open('mbox-short.txt')

num_list = []

for ln in fh:
    ln = ln.rstrip()
    if re.search('^New Revision: ([0-9]+)', ln):
        if len(re.findall('^New Revision: ([0-9]+)', ln)) > 0:
            num_list.append(float((re.findall('^New Revision: ([0-9]+)', ln))[0]))

# print(num_list)
print(f'New Revision: {int(sum(num_list)/len(num_list))}')