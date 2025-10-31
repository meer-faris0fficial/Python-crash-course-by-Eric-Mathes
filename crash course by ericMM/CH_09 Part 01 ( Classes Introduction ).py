#  Making an object from a class is called instantiation, and we work with instances of the classes
# a function in a class is called a method of the class

class dog:  # here dog is the class and the following are the objects
    def __init__(self,name,age): # self parameter is requires in method definition and is must come before other parameters
# init is called automatically when you create a new object from the class.
# Its job is to initialize the object’s attributes (give them values at the start)

        self.name = name # self.name is called instances
        self.age = age  # and variable like name/age that are accesible through these instances are called
                        # attributes
    
    def sit(self):
        print(f"{self.name} is now sitting.")
    
    def rollover(self):
        print(f"{self.name} rolled over.")

my_dog = dog('bam',1.5)
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()   
my_dog.rollover()

# Working with Classes and Instances
# global attribute place out side at the start of the class or any function 

class cars:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        #  Setting a Default Value for an Attribute
        self.speed = 0  # it is called default value 
        
    def get_discriptive(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def car_speed(self):
        print(f"this car has {self.speed} odometer.")
    
    #  Modifying an Attribute’s Value Through a Method
    def update_speed(self,mileage):
        
        if mileage >= self.speed:
            self.speed = mileage
        else:
            print("you cannot roll back an odometer.")
            
    #  Incrementing an Attribute’s Value Through a Method
    def increment_odometer(self,miles):
         """Add the given amount to the odometer reading."""
         self.speed += miles
            
          
my_newcar = cars('audi', 'a4', 2019)
print(my_newcar.get_discriptive())

my_newcar.update_speed(12000)  # this will update the car_speed argument
my_newcar.car_speed()

# adding the increment to the increment method
my_newcar.increment_odometer(500)
my_newcar.car_speed()

# output of the modifying attribute through a method
my_newcar.update_speed(65)  # this will update the speed of the car and put it in the car_speed
my_newcar.car_speed()

# out put of the changing the instannces attribute
# this is called instance value and it chnages the default value
my_newcar.speed = 45 # here function call uses the attribute name
my_newcar.car_speed()



