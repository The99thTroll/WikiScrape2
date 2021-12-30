from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

data = []

url = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

page = requests.get(url)
soup = bs(page.text, 'html.parser')
starTable = soup.find_all('table')
tableRows = starTable[7].find_all('tr')

for tr in tableRows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    data.append(row)

names = []
distance =[]
radius = []
mass =[]

for i in range(1,len(data)):
    names.append(data[i][0])
    distance.append(data[i][5])
    mass.append(data[i][7])
    radius.append(data[i][8])

df2 = pd.DataFrame(list(zip(names,distance,mass,radius)),columns=['Star_Name','Distance','Mass','Radius'])
print(df2)

df2.to_csv('dwarf_stars.csv')