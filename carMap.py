import json
from bs4 import BeautifulSoup

# get content from html carMakes
file_CarMakes = open('CarMakes.html',encoding='utf8')
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

def exportjson(dict_CarMakes):
    with open("carMakesDict.json", 'w', encoding="utf-8") as outfile:
        json.dump(dict_CarMakes, outfile)
    return


def importjson(infilename):
    with open("carMakesDict.json", 'r', encoding="utf-8") as infile:
      data =  json.load(infile)
      print(data)
    return
