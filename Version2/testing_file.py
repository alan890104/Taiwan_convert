import re
import requests as req
from bs4 import BeautifulSoup as Soup
from uuid import _random_getnode as getnode
import IOT_destination
import IOT_GPS



url_dict = {}
with open(r"C:\Users\alan8\test543\project\url_dictionary.txt","r") as f:
    while True:
        name = f.readline()
        url  = f.readline()
        if not name or not url: break
        name = name.replace('\n','')
        url_dict[name] = url

# Point out the destination on the map of Taiwan , output format [lng,lat]
def select_destination():
    return IOT_destination.destination()

# Change longitude and latitude to chinese name
def convert_to_name(longitude=120.999686 , latitude=24.7851415):
    return IOT_GPS.your_location(longitude,latitude)

# The destination location @weather.com
def weather_url(location):
    try : 
        return url_dict[location]
    except:
        print('Location does not exist!')


coordinate = select_destination()
location = convert_to_name(coordinate[0],coordinate[1])
_url = weather_url(location)

print(location,_url)