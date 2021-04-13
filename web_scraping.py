# https://en.wikipedia.org/wiki/List_of_Indian_states_and_union_territories_by_literacy_rate
# https://en.wikipedia.org/wiki/List_of_states_and_union_territories_of_India_by_crime_rate
# https://en.wikipedia.org/wiki/Indian_states_ranking_by_availability_of_toilets
# Web Scraping Example using the Literacy rates in India

# BeautifulSoup Docs - https://www.crummy.com/software/BeautifulSoup/bs4/doc/

# Loading the required libraries
from bs4 import BeautifulSoup as bs
import requests
import re


r = requests.get('https://en.wikipedia.org/wiki/List_of_Indian_states_and_union_territories_by_literacy_rate')

soup = bs(r.content)

# print(soup.title)
print(soup.title.string)
# print(soup.prettify())

tables = soup.find_all('table', class_= 'wikitable sortable')
# print(tables)
for table in tables:
    print(table)
    print('--'*30)

