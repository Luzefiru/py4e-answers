fn = input('Enter file name: ')
try:
    fh = open(fn)
except:
    print('Enter a valid file!')
    exit()

words_list = dict()
for lines in fh:
    if lines.startswith('From ') == False:
        continue
    # print(lines)
    lines = lines.split()
    time = lines[5]
    hour = time.split(':')
    words_list[hour[0]] = words_list.get(hour[0], 0) + 1

# print(words_list.items())

sorted_list = (sorted([(k,v) for k,v in words_list.items()]))

# print(sorted_list)

for k,v in sorted_list:
    print(k,v)