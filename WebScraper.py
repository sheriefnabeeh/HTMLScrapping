import requests, bs4, math

def ExtractPrices(inFileBS):
    inArray = inFileBS.select('body > div:nth-child(10) > div > section:nth-child(3) > div.row > div.large-8.columns > div > a > div > div.large-8.medium-8.small-12.columns.nopaddingRight.carData > div.row > div.large-3.medium-3.small-4.columns > span')
    priceArray = [0] * 10
    counterIndex = 0
    for x in inArray:
        string = x.get_text()
        counter = 0
        # print(string)
        number = 0
        for i in range(len(string)):
            if(string[len(string)-1-i].isdigit()):
                number += int(string[len(string)-1-i])*pow(10,counter)
                counter += 1
        priceArray[counterIndex] = number
        counterIndex += 1
    return priceArray

def ExtractYearOfMake(inFileBS):
    inArray = inFileBS.select('body > div:nth-child(10) > div > section:nth-child(3) > div.row > div.large-8.columns > div > a > div > div.large-8.medium-8.small-12.columns.nopaddingRight.carData > div.row > div.large-9.medium-9.small-8.columns.nopaddingRight > p')
    yearOfMakeArray = [0] * 10
    counterIndex = 0
    for x in inArray:
        yearOfMake = 0
        string = x.get_text()
        yearOfMake = string[string.index(" - ")+3:string.index(" - ")+7]
        yearOfMakeArray[counterIndex] = int(yearOfMake)
        counterIndex += 1
    return yearOfMakeArray


testFile = open('testcontactcars.html', encoding='utf8')
testFileBS = bs4.BeautifulSoup(testFile, 'html.parser')

print(ExtractPrices(testFileBS))
print(ExtractYearOfMake(testFileBS))
# testarray = testFileBS.select('body > div:nth-child(10) > div > section:nth-child(3) > div.row > div.large-8.columns > div > a > div > div.large-8.medium-8.small-12.columns.nopaddingRight.carData > div.row > div.large-3.medium-3.small-4.columns > span')
# teststring = testarray[0].get_text()
# testint = extractPrice(teststring)
# print(testint)
# print(testarray)
# print(testarray)