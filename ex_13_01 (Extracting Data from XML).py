# import urllib & XML Element Tree parsing libraries
import urllib.parse, urllib.error, urllib.request
import xml.etree.ElementTree as ET

# asks user to input URL with XML data, prints message of retrieval
url = input('Enter location: ')
print(f'Retrieving {url}')

# uses urllib library to urlopen the url, use .read() to save the entire XML file into the string 'xml'
xml = urllib.request.urlopen(url).read()

# prints the character length of the XML file: string xml
print(f'Retrieved {len(xml)} characters')

# using ElementTree XML parser to find all sub-elements under "{top element}/comments/comment" directory
# places all these elements into an iterable: 'lst'
xml = ET.fromstring(xml)
lst = xml.findall('comments/comment')

# for each element, append to 'num_list' the textual content (using .find & .text), which is the number, as a string
num_list = []
for ind in lst:
    num_list.append(int((ind.find('count').text)))

# using the list we made of all the numbers, print the tally of the numbers & its summation
print(f'Count: {len(num_list)}')
print(f'Sum: {sum(num_list)}')