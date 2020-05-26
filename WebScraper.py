import requests, bs4, time

def ReadDataFromContactCars(carmake, carmodel):
    pageNo = 1 
    arrayOfCars = []
    counterEndFlag = 0
    endFlag = 1

    while(endFlag):
        print('Requesting page in 5 seconds...')
        time.sleep(5)
        webstr = 'https://www.contactcars.com/usedcars?search=uc&mk=' + str(carmake) + '&md=' + str(carmodel) + '&page='+ str(pageNo)
        print(webstr)

        res = requests.get(webstr)
        res.raise_for_status()
        testFileBS = bs4.BeautifulSoup(res.text, 'html.parser')

        for i in testFileBS.select('div[carid]'):
            arrayOfData = [int(i.find('input')['data-id']), int(i.find('input')['data-price']), int(i.find('input')['data-year'])]
            arrayOfCars.append(arrayOfData)
            counterEndFlag += 1

        print("Number of cars found in page "+ str(pageNo) + ": " + str(counterEndFlag) + " car(s)")
        if(counterEndFlag == 0):
            print('All car ads have been collected.\n\n')
            endFlag = 0
        counterEndFlag = 0
        pageNo += 1
    
    return arrayOfCars

print(ReadDataFromContactCars(6,19))
### TODO ##
# Since ads are sorted by date of creation, to minimize unnecessary collection of data
# we can compare the carid in the for loop to the latest car id stored in our database
# and end data collection when a match is found. But first we need to find a way to
# store our data
