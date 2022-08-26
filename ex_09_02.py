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
    words_list[lines[2]] = words_list.get(lines[2], 0) + 1

print(words_list)