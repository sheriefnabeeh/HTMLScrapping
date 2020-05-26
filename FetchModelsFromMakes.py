from bs4 import BeautifulSoup

# get content from html carMakes
file_CarMakes = open('OpelContactCars.html', 'r', encoding='utf-8')
parsed = BeautifulSoup(file_CarMakes, 'html.parser')
dict = {}

for opt in parsed.findAll('select', attrs={'id': 'ucadvmodels'}):
    inn = opt.findAll('option')

# print(inn)
i = 0
for opt in inn:
    if (i == 0):
        i += 1
        continue
    dict[opt.get('value')] = opt.get_text()

print(dict)

# select brand, name, mileage
# from table_e3lanat , table_json
# join table_e3lanat & table_json on brand_value
# brand = 1 & model =3
