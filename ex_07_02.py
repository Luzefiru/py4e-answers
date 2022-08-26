fn = input('What file do you want to scan? ')
if fn == 'na na boo boo':
    print("NA NA BOO BOO TO YOU - You have been punk'd!")
    exit()

try:
    fn = open(fn)
except:
    print('ERROR: That is not a valid file!')
    exit()

count = 0
total_sc = 0
for ln in fn:
    if ln.startswith("X-DSPAM-Confidence:"):
        pos = ln.find(' ') + 1
        sc = ln[pos:]
        total_sc = total_sc + float(sc)
        count = count + 1

print('Average spam confidence:', (total_sc/count))