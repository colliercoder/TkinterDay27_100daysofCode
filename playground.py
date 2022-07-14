def add(*args):

    print(args[0])
    sum = 0
    for n in args:
        sum+=n

    return sum
print(add(2,3,2,5,2,3,5,52,5,52,5,6,22,5,7,92,987))

def calculate(n,**kwargs):
    print(kwargs)
    for key,value in kwargs.items():
        print(key,value)
    print(kwargs["add"])
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2,add = 3, multiply = 5)

class Car:

    def __init__(self,**kwargs):
        self.make = kwargs["make"]
        self.model = kwargs["model"]
        self.mpg = kwargs.get("mpg")
        self.color = kwargs.get("color")

my_car = Car(make = "toyota", model="tacoma", mpg = 10000, color="green")

print(my_car.model,my_car.make, my_car.mpg,my_car.color)
