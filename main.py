import apicall
print(f"The fare for the Cheapest flight for the date:  is: {apicall.cheapestPrice} INR\nThe website link to book the ticket is: {apicall.websiteLink}")

date = f"{apicall.yearofTravel}-{apicall.monthofTravel}-{apicall.dateofTravel}"
departureCode = apicall.departurecityCode
arrivalCode = apicall.arrivalcityCode
typeofTrip = apicall.typeofTrip
typeofClass = apicall.typeofClass

class User():
    def __init__(self, name, email, phno):
        self.name = name
        self.email = email
        self.phno = phno
    
class Search():
    def __init__(self):
        self.presentLocation = ""
        self.Destination = ""
        self.DateofTravel = ""
        self.MonthofTravel = ""
        self.YearofTravel = ""

    def getInput(self):
        self.presentLocation = input("Enter your From location: ")
        self.Destination = input("Enter your Destination: ")
        self.DateofTravel = input("Enter your Date of Travel: ")
        self.MonthofTravel = input("Enter your Month of Travel: ")
        self.YearofTravel = input("Enter your Year of Travel: ")
        print(f'\nThe Entered Details are: \nFrom: self.presentLocation. \nTo: {self.Destination}, \nDate of Travel: {self.DateofTravel}/{self.MonthofTravel}/{self.YearofTravel}')
        a = input("Are these Details Correct? (Y/N): ")
        if a == "Y":
            print("Thank You for your Details.")
        else:
            Search().getInput()
        modeofTravel = input("Enter the mode of Travel: 1) Train\n2) Flight: ")
        if(modeofTravel == "1"):
            print(" Please Wait while we look for the available trains. :) ")
        elif(modeofTravel == "2"):
            print(" Please Wait while we look for the available flights. :) ")
            
# class Traininfo():
#     def __init__(self, TrainName, TrainNumber, TrainArrivalTime, TrainDepartureTime, TrainFare, TrainDuration, TrainAvailability):
#             self.TrainName = TrainName
#             self.TrainNumber = TrainNumber
#             self.TrainArrivalTime = TrainArrivalTime
#             self.TrainDepartureTime = TrainDepartureTime
#             self.TrainFare = TrainFare
#             self.TrainDuration = TrainDuration
#             self.TrainAvailability = TrainAvailability
            
#     def printInfo(self):
#             print(f"\nTrain name: {self.TrainName} \nTrain Number: {self.TrainNumber} \nTrain Arrival Time: {self.TrainArrivalTime} \nTrain Departure Time: {self.TrainDepartureTime} \nTrain Fare: {self.TrainFare} \nTrain Duration: {self.TrainDuration} \nTrain Availability: {self.TrainAvailability}\n\n")

        
class Flightinfo():
    def __init__(self, FlightName, FlightNumber, FlightArrivalTime, FlightDepartureTime, FlightFare, FlightDuration, FlightAvailability):
        self.FlightName = FlightName
        self.FlightNumber = FlightNumber
        self.FlightArrivalTime = FlightArrivalTime
        self.FlightDepartureTime = FlightDepartureTime
        self.FlightFare = FlightFare
        self.FlightDuration = FlightDuration
        self.FlightAvailability = FlightAvailability
        
    def printInfo(self):
        print(f'\n Flight Name: {self.FlightName} \n Flight Number: {self.FlightNumber} \n Flight Arrival Time: {self.FlightArrivalTime} \n Flight Departure Time: {self.FlightDepartureTime} \n Flight Fare: {self.FlightFare} \n Flight Duration: {self.FlightDuration} \n Flight Availability: {self.FlightAvailability}\n\n')

Flights = {
                "Air India": ["AI-123", "8:00", "12:00", "Rs. 6000", "1 hours 45 Minutes", "Available"], 
                "Indigo": ["IN-123", "10:00", "12:00", "Rs. 15000", "3 hours", "Available"], 
                "Spice Jet": ["SJ-123", "10:00", "12:00", "Rs. 5000", "2 hours", "Available"], 
                "Go Air": ["GA-123", "10:00", "12:00", "Rs. 5000", "2 hours", "Available"], 
                "Vistara": ["VT-123", "10:00", "12:00", "Rs. 5000", "2 hours", "Available"]
            }
# Trains = {  
#                 "Rajdhani Express": ["RJ-123", "10:00", "12:00", "Rs. 5000", "2 hours", "Available"], 
#                 "Shatabdi Express": ["ST-123", "10:00", "12:00", "Rs. 5000", "2 hours", "Available"], 
#                 "Duronto Express": ["DT-123", "10:00", "12:00", "Rs. 5000", "2 hours", "Available"], 
#                 "Garib Rath Express": ["GR-123", "10:00", "12:00", "Rs. 5000", "2 hours", "Available"], 
#                 "Tejas Express": ["TJ-123", "10:00", "12:00", "Rs. 5000", "2 hours", "Available"]
#             }
A = list(Flights.keys())
# B = list(Trains.keys())

UserA = User("Sid", "siddharthreddy2812@gmail.com", "6281287188")
F = {}
# print("Available Flights are: \n")
for i in range(len(A)):
    F[i] = Flightinfo(A[i],Flights[A[i]][0], Flights[A[i]][1], Flights[A[i]][2], Flights[A[i]][3], Flights[A[i]][4], Flights[A[i]][5])
    # F[i].printInfo()
# T = {}
# # print("Available Trains are: \n")
# for i in range(len(B)):
#     T[i] = Traininfo(B[i],Trains[B[i]][0], Trains[B[i]][1], Trains[B[i]][2], Trains[B[i]][3], Trains[B[i]][4], Trains[B[i]][5])
    # T[i].printInfo()