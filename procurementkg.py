import requests
import json
from bs4 import BeautifulSoup
import pandas as pd
import xlwt
url = "http://procurement.kg/list/page/2"


r = requests.get(url).text
print(r)
soup = BeautifulSoup(r, "html.parser")


soup = soup.find('ul', {'class': 'list-group home-tenders'}).find_all('li', {'class': 'tender-item list-group-item row flex'})
result  = soup
list1 = []
list2 = []
list3 = []
list4 = []
list5 = []
list6 = []
list7 = []

for i in result:
  name_comp = i.find('h3', {'class': 'company-name'})
  type_bussiness = i.find('div', {'class': 'type'})
  type_deal = i.find('span', {'class': 'badge'})
  title = i.find('h2', {'class': 'position'})
  date_creating = i.find('div', {'class': 'created'})
  deadline= i.find('div', {'class': 'due'})
  place = i.find('div', {'class': 'location'}).find('span')
  #print(type_deal.get_text(strip=True))
  list1.append((name_comp.text).strip())
  list2.append((type_bussiness.text).strip())
  list3.append((type_deal.text).strip())
  list4.append((title.text).strip())
  list5.append((date_creating.text).strip())
  list6.append((deadline.text).strip())
  list7.append((place.text).strip())

"""
try:
  for i in result:
    type_deal = i.find('span', {'class': 'badge'})
    if type(type_deal) != 'NoneType'
      print(type(type_deal))
      print(type_deal.get_text(strip=True))
    else:
      print("google")
except AttributeError:
  print("Miss")
  pass

"""

  

#   x = name_comp.text
#   print(x.strip())
#   print((type_bussiness.text).strip())
#  print(type_deal.text).strip())
#   print(title.text.strip())
#   print(date_creating.text.strip())
#   print(deadline.text.strip())
#   print(place.text.strip())
#   print("================================")


df = pd.DataFrame()
data = pd.DataFrame({"Name of Company": list1, "Type of business": list2,"type of deal": list3, "Title": list4, "Start Date": list5, "Due Date": list6, "Location": list7})
df = df.append(data)
print(df)
outputFile = "data.xls"
with pd.ExcelWriter(outputFile) as ew:
    df.to_excel(ew, startrow=3, startcol=2)

"""
def get_num_pages(url):
  try:
    r = requests.get(url).text
    soup = BeautifulSoup(r, "html.parser")
    soup = soup.find('ul', {'class': 'pagination'}).find('a', {'class': 'page-numbers'})
    result = soup.get('href')
    lis1 = []
    lis1.append(result)
    for url1 in lis1:
      print()
      r1 = requests.get(url1).text
      soup = BeautifulSoup(r1, "html.parser")
      soup = soup.find('ul', {'class': 'pagination'}).find('a', {'class': 'next page-numbers'})
      result1 = soup.get('href')
      lis1.append(result1)
    return lis1
  except AttributeError:
      return lis1
"""