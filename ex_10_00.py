fh = open('intro.txt')

words_list = dict()
frequency = 0
most_frequent = None
for lines in fh:
    lines = lines.split()
    for word in lines:
        words_list[word] = words_list.get(word, 0) + 1
        if frequency == 0 or frequency < words_list[word]:
            frequency += 1
            most_frequent = word

# print(words_list)

sorted_list = (sorted([(v, k) for (k,v) in words_list.items()], reverse = True))

for v,k in sorted_list[:5]:
    print(f'The word {k} has a frequency of {v}')
# print(f"\nHere's the most frequent word: {most_frequent}, with a freuqnecy of {words_list[most_frequent]}.")