# variable initialization
number_list = []
largest = None
smallest = None

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
    
    # Boolean Expressions for saving largest & smallest numbers
    if largest is None:
        largest = float_user_number
    elif float_user_number > largest:
        largest = float_user_number

    if smallest is None:
        smallest = float_user_number
    elif float_user_number < smallest:
        smallest = float_user_number    

    # list concatenation
    number_list = number_list + [float_user_number]

# prints the list
# print(number_list, "\n")

# prints maximum & minimum of the list
print('Maximum is', int(largest))
print('Minimum is', int(smallest))