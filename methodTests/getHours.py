import requests
from bs4 import BeautifulSoup

def parse(s):
    type = s[len(s)-2:]
    o = int(s[:len(s)-2])
    if(type == 'pm'):
        o += 12
    return o
# document.querySelector('.columns table').querySelectorAll('tr')[1].querySelectorAll('td')[2].textContent.split(' ')
# Making a GET request
r = requests.get("https://www.rit.edu/fa/arenas/gordon-field-house/facility-hours")
 
# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')

s = soup.find('div', class_='columns').find('table').find_all('tr')[1].find_all('td')[2]
content = s.string.split(' ')

print(parse(content[0]), parse(content[2]))
