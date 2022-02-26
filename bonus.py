import pandas as pd

zips = pd.Series({'Boston': '02215', 'Miami': '3310'})
print(zips.str.match(r'\d{5}'))

cities = pd.Series(['Boston, MA 02215', 'Miami, FL 33101'])
print(cities.str.contains(r' [A-Z]{2}'))
print(cities.str.match(r' [A-Z]{2} '))

contacts = [['Mike Green', 'demo1@deitel.com', '5555555555'], ['Sue Brown', 'demo2@#deitel.com', '5555551234']]
contactsdf = pd.DataFrame(contacts, columns=['Name', 'Email', 'Phone'])

print(contactsdf)