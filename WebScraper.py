import requests, bs4, math

def extractPrice(inString):
    counter = 0
    number = 0
    for i in range(len(inString)):
        if(inString[len(inString)-1-i].isdigit()):
            number += int(inString[len(inString)-1-i])*pow(10,counter)
            counter+=1
    return number

testFile = open('testcontactcars.html', encoding='utf8')
testFileBS = bs4.BeautifulSoup(testFile, 'html.parser')

testarray = testFileBS.select('body > div:nth-child(10) > div > section:nth-child(3) > div.row > div.large-8.columns > div > a > div > div.large-8.medium-8.small-12.columns.nopaddingRight.carData > div.row > div.large-3.medium-3.small-4.columns > span')
teststring = testarray[0].get_text()
testint = extractPrice(teststring)
print(testint)

print(testarray)
