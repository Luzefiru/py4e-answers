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
    atpos = lines.find('@')
    spacepos = lines.find('\n', atpos)
    # print(atpos, spacepos)

    words_list[lines[atpos:spacepos]] = words_list.get(lines[atpos:spacepos], 0) + 1

print(words_list)