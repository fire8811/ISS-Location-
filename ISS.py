import requests
import json

#*** get coordinates of ISS***
ISSurl = "http://api.open-notify.org/iss-now.json"
r = requests.get(ISSurl)

data = r.json()

lat = data["iss_position"]['latitude']
lon = data["iss_position"]['longitude']

print("ISS LATITUDE: ", lat)
print("ISS LONGITUDE: ", lon)

coords = str(lat)+ "," + str(lon) #change coords into one string

#***Reverse geocode coordinates to get location***
geoKey = #FREE API KEY HERE (https://positionstack.com/)
payload = {'access_key':geoKey, 'query':coords}

geoResponse = requests.get("http://api.positionstack.com/v1/reverse", params=payload) #reverse geocoding


geoData = geoResponse.json() #turn results into json 

if(geoData['data'][0]['country'] == None): #check if over water
    location = geoData['data'][0]['name']
    print("The ISS is over the", location) #print ocean/sea name
else:
    location = geoData['data'][0]['country']
    print("The ISS is over", location) #print country name