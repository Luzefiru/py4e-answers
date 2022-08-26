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

frequency = None
most_frequent = None
for email,count in words_list.items():
    if frequency == None or frequency < count:
        frequency = count
        most_frequent = email

print(most_frequent, frequency)

