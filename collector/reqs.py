import requests
from bs4 import BeautifulSoup
from os import environ as env

serverIP = env.get('serverIP', 'http://127.0.0.1:8000')

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

def submit(data):
       r = requests.post(serverIP + "/submit", json=data)
       print("sent data with code: " + str(r.status_code))