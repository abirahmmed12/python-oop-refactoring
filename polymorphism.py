# class Payment:
#     def process_payment(self,amount):
#         print(f"processing Bkash payment of {amount} taka")


# class Bkash(Payment):
#     def process_payment(self, amount):
#         print(f"Processing Bkash payment of {amount} taka. SMS notification sent!")

# class Card(Payment):
#     def process_payment(self, amount):
#         print(f"Processing Credit Card payment of {amount}taka. 2% tax applied!")

# payment_bkash=Bkash()
# payment_card=Card()

# payment_card.process_payment(500)
# payment_bkash.process_payment(500)


#

class Ride:
    def calculate_fare(self,distance):
        rent=distance*10
        print(rent)

class BikeRide(Ride):
    def calculate_fare(self, distance):
        bike_cost=distance*8
        print(bike_cost)

class CarRide(Ride):
    def calculate_fare(self, distance):
        car_cost=(distance*15)+50
        print(car_cost)

class AmbulanceRide(Ride):
    ambulance_cost=0
    print(ambulance_cost)

rides=[BikeRide(),CarRide(),AmbulanceRide()]

for ride in rides:
    ride.calculate_fare(10)