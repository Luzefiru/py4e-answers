# variable initialization
number_list = []
number_count = 0
number_total = 0

# loops & saves numbers until 'done' is inputted
while True:
    user_number = input('Enter a number: ')
    if user_number == 'done':
        break
    else:
        try:
            float_user_number = float(user_number)
        except:
            print('Invalid input')
            continue

    # mathematical expression to save data then loops back to 'while'    
    number_count = number_count + 1
    number_total = number_total + float_user_number

    # list concatenation
    number_list = number_list + [float_user_number]

# prints the list
# print(number_list, "\n")

# prints maximum & minimum of the list
print('Maximum is', int(max(number_list)))
print('Minimum is', int(min(number_list)))