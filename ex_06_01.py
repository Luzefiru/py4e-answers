fruit = 'banana'

# sets index to length of 'banana' but minus 1 to acount for the 0th place.
index = (len(fruit)-1)

# as long as index is greater than -1, so 0 to the farthest index, the code prints the letters of 'banana' backwards
while index > -1:
    letter = fruit[index]
    print(letter)
    index = index - 1