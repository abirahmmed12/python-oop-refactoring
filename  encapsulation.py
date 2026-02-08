# class WaterBottle:
#     def __init__(self):
#         self.__water_level=0


#     def fill_water(self,ml):
#         if ml>0:
#             self.__water_level+=ml
#             print(f"{ml} has been filled in the bottle")
#         else:
#             print(" the amount cant be less then zero")

#     def drink_water(self,ml):
#         if ml<=self.__water_level:
#             self.__water_level-=ml
#             print(f"you have drink {ml} water")
#         else:
#             print('you do not have enough water in your bottle')

#     def rest_water(self):
#         print(f"you have {self.__water_level} ml water in your bottle")


# my_bottle=WaterBottle()

# my_bottle.fill_water(500)


# my_bottle.__water_level=1000
# print(my_bottle.__water_level)
# my_bottle.rest_water()


class MObile:
    def __init__(self):
        self.__battery_level=100

    def use_app(self,minutes):
        charge_need=minutes*5
        if self.__battery_level>=5 and self.__battery_level>=charge_need:
            self.__battery_level-=charge_need
            print(f"after using {minutes} the btry is {self.__battery_level}")

        else:
            print('not enough charge')

def charge_phone(self, amount):
        if amount > 0:
            self.__battery_level += amount
            
            
            if self.__battery_level > 100:
                self.__battery_level = 100
                print("full")
            else:
                print(f": {self.__battery_level}%")
        else:
            print("wrong")