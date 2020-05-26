import codecs
from html.parser import HTMLParser
from bs4 import BeautifulSoup

# get content from html carMakes
file_CarMakes = codecs.open('CarMakes.html', 'r', 'utf-8')
parsed = BeautifulSoup(file_CarMakes, 'html.parser')
# print(parsed.find_all('option'))

# initializing variables for loop and dictionary
i = 1
dict_CarMakes = {}

for single in parsed.findAll('option'):
    # dict_CarMakes.update({single.get('value'): single.get_text()})
    dict_CarMakes[single.get('value')] = single.get_text()
    i += 1

print(dict_CarMakes)
