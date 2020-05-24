import requests, bs4, math
# BMW 320i
testFile = open('testcontactcars.html', encoding='utf8')
testFileBS = bs4.BeautifulSoup(testFile, 'html.parser')

for i in testFileBS.select('div[carid]'):
    print([int(i.find('input')['data-id']), int(i.find('input')['data-price']), int(i.find('input')['data-year'])])