import requests
from bs4 import BeautifulSoup
from os import environ as env
from schedule import CancelJob

serverIP = env.get('serverIP', 'http://localhost:8080')

def getFacilityOccupancy():
    print("Getting occupancy")
    # Making a GET request
    r = requests.get('https://recreation.rit.edu/facilityoccupancy')

    # Parsing the HTML
    soup = BeautifulSoup(r.content, 'html.parser')

    s = soup.find_all('div', class_='d-md-flex')
    out = {'lower': s[0].find(class_='occupancy-count').string,
           'upper': s[1].find(class_='occupancy-count').string,
           'aquatics': s[2].find(class_='occupancy-count').string
           }

    submit(out)
    return CancelJob

def submit(data):
       r = requests.post(serverIP + "/submit", json=data)
       print("sent data with code: " + str(r.status_code))


def parse(s):
    type = s[len(s)-2:]
    o = int(s[:len(s)-2])
    if(type == 'pm'):
        o += 12
    return o
# document.querySelector('.columns table').querySelectorAll('tr')[1].querySelectorAll('td')[2].textContent.split(' ')
# Making a GET request
def getStartEndHour():
       r = requests.get("https://www.rit.edu/fitnessrecreation/facility-hours")
       
       # Parsing the HTML
       soup = BeautifulSoup(r.content, 'html.parser')
       
       s = soup.select_one(".facility-hours td")
       content = s.string.split(' ')

       return(parse(content[0]), parse(content[2]))
