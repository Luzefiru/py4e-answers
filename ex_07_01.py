fh = open('mbox-short.txt', 'r', encoding='UTF-8')
print(fh)

for lx in fh:
    ly = lx.rstrip()
    print(ly.upper())