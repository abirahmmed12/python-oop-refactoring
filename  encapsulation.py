class WaterBottle:
    def __init__(self):
        self.__water_level=0


    def fill_water(self,ml):
        if ml>0:
            self.__water_level+=ml
            print(f"{ml} has been filled in the bottle")
        else:
            print(" the amount cant be less then zero")

    def drink_water(self,ml):
        if ml<=self.__water_level:
            self.__water_level-=ml
            print(f"you have drink {ml} water")
        else:
            print('you do not have enough water in your bottle')

    def rest_water(self):
        print(f"you have {self.__water_level} ml water in your bottle")


my_bottle=WaterBottle()

my_bottle.fill_water(500)


my_bottle.__water_level=1000
print(my_bottle.__water_level)
my_bottle.rest_water()
