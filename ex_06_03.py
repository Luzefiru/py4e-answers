string = input('What kind of string do you want to scan? ')
scanned_string = input('What substring do you want to scan for? ')

def count(string, scanned_string):
    count = 0
    for index in string:
        if index == scanned_string:
            count = count + 1
    return count

print('Here is how many times', "'" + scanned_string + "'", 'showed up:', count(string, scanned_string))