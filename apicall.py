import requests
import json
# import main

dateofTravel = input("Enter the date of travel: ")
monthofTravel = input("Enter the month of travel: ")
yearofTravel = input("Enter the year of travel: ")
departurecityCode = input("Enter the departure city code: ")
arrivalcityCode =  input("Enter the arrival city code: ")
typeTrip = input("Enter the type of trip: \n1) One Way\n2) Round Trip\n>")
if typeTrip == "1":
    typeofTrip = "onewaytrip"
elif typeTrip == "2":
    typeofTrip = "roundtrip"
numadults = input("Enter the number of adults: ")
numchildren = input("Enter the number of children: ")
numinfants = input("Enter the number of infants: ")

typeClass = input("Enter the type of class: \n1) Economy\n2) Business\n3) First\n>")
if typeClass == "1":
    typeofClass = "Economy"
elif typeClass == "2":
    typeofClass = "Business"
elif typeClass == "3":
    typeofClass = "First"

print("\nTaking default Currency as INR.\n\n")



# url = f"https://api.flightapi.io/{typeofTrip}/63c59729a9ae3312a63e72bf/{departurecityCode}/{arrivalcityCode}/{yearofTravel}-{monthofTravel}-{dateofTravel}/{numadults}/{numchildren}/{numinfants}/{typeofClass}/INR"
# print(url)
# payload={}
# headers = {}

# data = requests.request("GET", url, headers=headers, data=payload)
# a = json.loads(data.text)
# print(data)
data = open('response.json', 'r')
a = json.load(data)
# print(a)

totalAvailableFlights = len(a['airlines'])
print("Total available number of flights: ", totalAvailableFlights)   
# print(totalAvailableFlights)
allFlights = []
allFlights_codes = []
for i in range(totalAvailableFlights):
    allFlights.append(a['airlines'][i]['name'])
    allFlights_codes.append(a['airlines'][i]['code'])
    j  = a['filters']['airlines'][i]['price']['totalAmount']
    k = a['filters']['airlines'][i]['code']
    print(k)
    print(j)



print(allFlights)
print(allFlights_codes)

# print(a['airlines']['code'])


departureCity_code = a['search']['legs'][0]['departureCity']['code']
departureCity_name = a['search']['legs'][0]['departureCity']['enName']

arrivalCity_code = a['search']['legs'][0]['arrivalCity']['code']
arrivalCity_name = a['search']['legs'][0]['arrivalCity']['enName']

cheapestPrice = a['filters']['minPrice']['totalAmount']
# print(a['filters']['minPrice'])

websiteLink= a['fares'][0]['handoffUrl']

class flightDetails():
    def __init__(self, flightName):
        self.flightName = flightName
        # self.
        self.flighDetails = {    
                            "flightName": "Air India",
                            "flightCode": "AI",
                            "flightPrice": "INR 10000",
                            "flightDepartureTime": "10:00",
                            "flightArrivalTime": "12:00",
                            "flightDuration": "2 hours",
                            "flightStops": "0",
                            "flightDepartureCity": "DEL",
                            }

    def getFlightDetails(self):
        return self.flighDetails

print(flightDetails("Air India").getFlightDetails())