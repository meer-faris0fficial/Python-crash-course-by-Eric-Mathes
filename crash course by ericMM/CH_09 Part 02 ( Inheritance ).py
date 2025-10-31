# inheritance
# If the class you’re writing is a specialized version of another class you wrote, you can use inheritance.
# When one class inherits from another, it takes on the attributes and methods of the first class.
# The original class is called the parentclass, and the new class is the child class. The child class
# can inherit any or all of the attributes and methods of its parent class, but it’s also free to 
# define new attributes and methods of its own.

#  The __init__() Method for a Child Class the __init__ method of the child class can use to call the any
# method of the parent class

class Car:
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        self.fuel = 10
        
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.model} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")
        
    def update_odometer(self, mileage):
        
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
            
    def increment_odometer(self, miles):
        self.odometer_reading += miles
        
    def fuel_tank(self):
        print(f"the fuel tank capacity of the car is {self.fuel} litres.")

 # instances as attributes
class Battery:
    """A simple attempt to model a battery for an electric car."""
    def __init__(self, battery_size=75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")
    def get_range(self):
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        else:
            print("the range of the car is not specific.")
        # without the return statement the get_range function will continue to execute and as there is no 
        # assign value for each battery size so therefore it will give an error as it goes to print statement
        # so the return statement is must to avoid the error and stop the execution
            return   
        print(f"the car can go about {range} miles on the full charge.")        
        
class Electric_car(Car):
    """the car in the bracket is use to call the parent class"""
    def __init__(self, make, model, year):
        """super().__init__() is a special method that is use to call the method from the parent class"""
        super().__init__(make, model, year)  
        self.battery = Battery() # initiallize the class the battery class
        
        
    # def battery_size(self):
    #     print(f"the size of the battery is {self.battery}")
        
    #  Overriding Methods from the Parent Class 
    """Python disregard the method of the parent class and pay attention only to the child class method"""
    # but tht overriding method must have the same name
    def fuel_tank(self):
        print("this car do not have a fuel tank.") # this will override the parent class method 
    
my_tesla = Electric_car('tesla','model s','2019')
print(my_tesla.get_descriptive_name())
# my_tesla.battery_size()
my_tesla.fuel_tank()

#.battry below is from the self.battery to call the Battery class 
my_tesla.battery.describe_battery() # first call the electricCar class then BatteryClass then describe_battery method
my_tesla.battery.get_range()



    