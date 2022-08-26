fname = input('Enter file name: ')
fname = open(fname)

count = 0
for ln in fname:
    if (len(ln) != 0 and ln.startswith('From ')) is not True: continue
    ln = ln.split()
    print(ln[1])
    count = count + 1

print(f'There were {count} lines in the file with From as the first word')