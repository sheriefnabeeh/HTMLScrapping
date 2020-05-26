import codecs
from html.parser import HTMLParser

import csv
from bs4 import BeautifulSoup

# get content from html carMakes
file_CarMakes = codecs.open('CarMakes.html', 'r', 'utf-8')
parsed = BeautifulSoup(file_CarMakes, 'html.parser')
# print(parsed.find_all('option'))

# initializing variables for loop and dictionary
dict_CarMakes = {}
i = 0
for single in parsed.findAll('option'):
    if i == 0:
        i += 1
        continue
    # dict_CarMakes.update({single.get('value'): single.get_text()})
    dict_CarMakes[single.get('value')] = single.get_text()

print(dict_CarMakes)


def exportcsv(dict_CarMakes):
    writer = csv.writer(open("CarMakesDict", "w", encoding='utf-8'))
    for key, value in dict_CarMakes.items():
        writer.writerow([key, value])
    return


exportcsv(dict_CarMakes)
