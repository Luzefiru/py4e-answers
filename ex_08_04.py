romeo = open('romeo.txt')

filtered_list = list()

for ln in romeo:
    list_words = ln.split()
    for scan in list_words:
        if (scan in filtered_list) == False:
            filtered_list.append(scan)

filtered_list.sort()
print(filtered_list)