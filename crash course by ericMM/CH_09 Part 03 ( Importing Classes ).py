# Importing Classes

from CH09_Cars import Car

my_car = Car('Audi','a4','2019')
print(my_car.get_descriptive_name())

my_car.odometer_reading = 45
my_car.read_odometer()

from CH09_Cars import ElectricCar

my_tesla = ElectricCar('tesla','tesla s',2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

# Importing Multiple Classes from a Module

from CH09_Cars import Car,ElectricCar
my_beetle = Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())
my_tesla = ElectricCar('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())

#  Importing an Entire Module

import CH09_Cars as C_E  #  Using Aliases(i.e nick names)
my_beetle = C_E.Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())
my_tesla = C_E.ElectricCar('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())

# Importing All Classes from a Module we uses *

from CH09_Cars import * # it will import all the classes and methods from a module
# however this method is not recomended as it causes many confusions and errors if main file and module have same classes and variable name

#  Importing a Module into a Module

#  The Python Standard Library
from random import randint
vaariable = randint(1,10)
print(vaariable)

from random import choice
players = ['charles', 'martina', 'michael', 'florence', 'eli']
first_up = choice(players)
print(first_up)


 