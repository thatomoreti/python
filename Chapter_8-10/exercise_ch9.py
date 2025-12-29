from restaurant import Restaurant
from random import randint
from random import sample

kfc=Restaurant('Kentucky Fried Chicken','Chicken')
print(f"{kfc.restaurant_name}")
print(f"{kfc.cuisine_type}")
kfc.describe_restaurant()
kfc.open_restaurant()

#9-3 Three Restaurants
debonairs=Restaurant('Debonairs Pizza','Pizza')
silverstars=Restaurant('Silverstars','Steak')
ronnies_ice_cream=Restaurant('Ronnies Ice Cream','Ice Cream')

debonairs.describe_restaurant()
debonairs.open_restaurant()

silverstars.describe_restaurant()
silverstars.open_restaurant()

ronnies_ice_cream.describe_restaurant()
ronnies_ice_cream.open_restaurant()

#9-3 Users 
class User:
    
    def __init__(self,first_name,last_name,age,gender,login_attempts=0):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.gender=gender
        self.login_attempts=login_attempts
        
    def describe_user(self):
        print(f"User First Name: {self.first_name}")
        print(f"User Last Name: {self.last_name}")
        print(f"User Age: {self.age}\t")
        print(f"Gender: {self.gender}\t")
        
    def greet_user(self):
        print(f"Hi {self.first_name}")

    def increment_login_attempts(self):
        self.login_attempts+=1
        return self.login_attempts
    
    def reset_login_attempts(self):
        self.login_attempts=0
        return self.login_attempts
    
steve=User('James','Madison',21,'Male')
steve.describe_user()
steve.greet_user()

xavi=User('Xavi','Modikwane',23,'Female')
xavi.describe_user()
xavi.greet_user()

thato=User('Thato','Moreti',21,'Male')
thato.describe_user()
thato.greet_user()

freddy=User('Freddy','Gibbs',26,'Male')
freddy.describe_user()
freddy.greet_user()

karabo=User('Karabo','Moreti',31,'Male')
karabo.describe_user()
karabo.greet_user()

#Car.py

class Car:
    def __init__(self,color,model,manufacturer):
        self.color=color
        self.model=model
        self.manufacturer=manufacturer
    
    def get_car_description(self):
        description=f"The {self.model} is created by {self.manufacturer} and it is {self.color}"
        return description
new_car=Car('blue','x-8','BMW')
d=new_car.get_car_description()
print(d)

#9-4 Number Served
pedros=Restaurant("Pedros","African")
print(pedros.number_served)

pedros.set_number_served(7)
print(pedros.number_served)

pedros.increment_number_served(100)
print(pedros.number_served)

#9-5 Login Attempts 
james=User('James','Madison',81,'Female',5)

james.increment_login_attempts()
print(james.login_attempts)

james.reset_login_attempts()    
print(james.login_attempts)

class Animal:
    def __init__(self,name):
        self.name=name
        self.ismamal=True
        self.isintroduced=False
    
    def animal_intro(self):
       print(f"This is a {self.name}") 
       self.isintroduced=True
    
    def mammal_check(self):
        if self.isintroduced:
            if self.ismamal:
                print(f"{self.name} is a mammal too")
        
class Tiger(Animal):
    def __init__(self, name):
        super().__init__(name)
        
    def roar(self):
        print(f"Roar!")

tiger=Tiger("Simba")

tiger.animal_intro()
tiger.mammal_check()
tiger.roar()

#9-6 Ice Cream Stand
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, number_served=0):
        super().__init__(restaurant_name, cuisine_type, number_served)
        self.flavor=['Vanilla','Chocolate','Strawberry','Kelp','Jalapeno']
        
    def show_flavors(self):
        print("Flavors on Sale:")
        for f in self.flavor:
            print(f"\t-{f}")
sallys=IceCreamStand("Sally's","Ice Cream")
sallys.show_flavors()

#9-8 Privileges
class Privileges:
    def __init__(self):
        self.privileges=['can add post','can delete post','can ban user','can suspend user']
        
    def show_privileges(self):
        print("As an Admin , you:")
        for p in self.privileges:
            print(f"\t-{p}")
            


#9-7 Admin 
class Admin(User):
    def __init__(self, first_name, last_name, age, gender, login_attempts=0):
        super().__init__(first_name, last_name, age, gender, login_attempts)
        self.privileges=Privileges()
        
sbu=Admin("Sbusiso","Dlomo",54,"Male")
sbu.privileges.show_privileges()

dave=Admin("Davido","Nkomo",34,"Female")
dave.privileges.show_privileges()

#9-9 Battery Upgrade
class Battery:
# """A simple attempt to model a battery for an electric car."""
    def __init__(self, battery_size=75):
# """Initialize the battery's attributes."""
        self.battery_size = battery_size
    def describe_battery(self):
        
# """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")
        
    def get_range(self):
# """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on a full charge.")
        
    def upgrade_battery(self):
        if self.battery_size==100:
            print("We're good here mate.")
        else:
            self.battery_size=100
class ElectricCar(Car):
    def __init__(self, color, model, manufacturer):
        super().__init__(color, model, manufacturer)
        self.battery=Battery()
        
tesla=ElectricCar('blue','Y-18','Tesla')
tesla.battery.get_range()
tesla.battery.upgrade_battery()
tesla.battery.get_range()

#9-13 Dice

class Die:
    def __init__(self,sides=6):
        self.sides=sides
        
    def roll_die(self):
        print(randint(1,self.sides))
        
six=Die()
six.roll_die()
six.roll_die()
six.roll_die()
six.roll_die()
six.roll_die()
six.roll_die()
six.roll_die()
six.roll_die()
six.roll_die()
six.roll_die()
six.roll_die()

ten=Die(10)
ten.roll_die()
ten.roll_die()
ten.roll_die()
ten.roll_die()
ten.roll_die()
ten.roll_die()
ten.roll_die()
ten.roll_die()
ten.roll_die()
ten.roll_die()

twenty=Die(20)
twenty.roll_die()
twenty.roll_die()
twenty.roll_die()
twenty.roll_die()
twenty.roll_die()
twenty.roll_die()
twenty.roll_die()
twenty.roll_die()
twenty.roll_die()
twenty.roll_die()


#9-14 Lottery
series=('K',1,2,3,4,'O',99,'l','P',6,8,6,10,19,21,'I')
random_choice=sample(series,4)
print(f"Any ticket that matches these numbers/letter wins: {random_choice}")


#9-15 Lottery Analysis
my_ticket=[1,'K',8,'I']
count=0
winning_numbers=[]
while my_ticket!= winning_numbers:
    count+=1
    winning_numbers=sample(series,4)
print(f"It took {count} times to win the lottery!Can you believe it?")

