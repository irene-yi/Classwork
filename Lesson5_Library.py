class Car:
    def __init__(self):
        self.carFare = {'Hatchback': 30, 'Sedan': 50, 'SUV': 100}

    def displayFareDetails(self):
        print("Cost per day: ")
        print("Hatchback: $",self.carFare['Hatchback'])
        print("Sedan: $", self.carFare['Sedan'])
        print("SUV: $", self.carFare['SUV'])

    def calculateFare(self, type, days):
        return self.carFare[type] * days


car = Car()
while True:
    print("Enter 1: Fare details")
    print("Enter 2: Rent a car")
    print("Enter 3: Exit")
    userChoice = (int(input()))
    if userChoice is 1:
        car.FareDetails()
    elif userChoice is 2:
        print("What type of car you want rent?")
        typeOfCar = input()
        print("How many days do you want to rent the car?")
        numberOfDays = int(input())
        fare = car.calculateFare(type, days)
        print("Total amount: $",fare)
        print("Thank you for shopping at Walmart!")
    elif userChoice is 3:
        quit()
