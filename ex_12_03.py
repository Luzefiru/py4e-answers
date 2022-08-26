import urllib.request, urllib.parse, urllib.error

inp = input('Please enter a URL: ')

try:
    characters = urllib.request.urlopen(inp).read()
except:
    print('ERROR: Invalid URL!')
    exit()

limited_chars = characters.decode()[:3000]

print(limited_chars)
print(f'\n\\\\ Overall number of characters/bytes of the original document = {len(characters)}')