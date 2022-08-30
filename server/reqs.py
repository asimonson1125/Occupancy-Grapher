import requests
from bs4 import BeautifulSoup
from init import submit


def getFacilityOccupancy():
    print("Getting occupancy")
    # Making a GET request
    r = requests.get('https://recreation.rit.edu/facilityoccupancy')

    # Parsing the HTML
    soup = BeautifulSoup(r.content, 'html.parser')

    s = soup.find_all('div', class_='d-md-flex')
    out = {"lower": s[0].find(class_='occupancy-count').string,
           "upper": s[1].find(class_='occupancy-count').string,
           "aquatics": s[2].find(class_='occupancy-count').string
           }

    submit(out)
