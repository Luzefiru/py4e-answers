fn = input('Enter file name: ')
try:
    fh = open(fn)
except:
    print('Enter a valid file!')
    exit()

# reads the file & then creates a list with just the alphabetical characters
converted = fh.read()
converted = [x for x in list(converted.lower()) if x.isalpha() is True]

# creates a letter histogram & counts the frequency using .get idiom
l_histogram = dict()
for x in converted:
    l_histogram[x] = l_histogram.get(x, 0) + 1

# list comprehension to create a sorted histogram by (value, key) tuples in the dictionary, by descending order
srt_histogram = sorted([(v,k) for k,v in l_histogram.items()], reverse = True)

# print(srt_histogram)

for v,k in srt_histogram:
    print (f"Letter '{k}' appeared: {v} times.")