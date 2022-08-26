fn = input('Enter file name: ')
try:
    fh = open(fn)
except:
    print('Enter a valid file!')
    exit()

words_list = dict()
for lines in fh:
    if lines.startswith('From:') == False:
        continue
    # print(lines)
    lines = lines.split()
    words_list[lines[1]] = words_list.get(lines[1], 0) + 1

# print(words_list.items())

sorted_list = (sorted([(v,k) for k,v in words_list.items()], reverse = True))

for v,k in sorted_list[0:1]:
    print(k,v)