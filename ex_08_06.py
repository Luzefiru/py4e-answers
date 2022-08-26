num_list = list()
inp = None

while inp != 'done':
    inp = input('Enter a number: ')
    try:
        float(inp)
        num_list.append(inp)
    except:
        if inp != 'done':
            print('ERROR: Please input a valid number!')
            continue


print(f'Maximum: {max(num_list)}\nMinimum: {min(num_list)}')