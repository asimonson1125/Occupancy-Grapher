import requests
from bs4 import BeautifulSoup
 
 
# Making a GET request
r = requests.get('https://recreation.rit.edu/facilityoccupancy')
 
# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')

s = soup.find_all('div', class_='d-md-flex')
content = s[0].find(class_='occupancy-count')
 
print(content.string)