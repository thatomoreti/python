#Creating a class, alongside its attributes and methods
class Cat:
    
    # initializes the class's / instantiates the Cat object attributes when called 
    def __init__(self,name,age,species):
        self.name=name
        self.age=age
        self.species=species
        
    #A Cat's methods
    def sit(self):
        print(f"{self.name} is a {self.species} and therefore now she's sitting")
    
    def purr(self):
        print(f"{self.name} is purring")
        
#Instantiate a cat
browns_cat=Cat('James',2,'Lion')

browns_cat.sit()
browns_cat.purr()
print(f"Brown's cat's name is {browns_cat.name}.")
print(f"Brown's cat's is {browns_cat.age} years old.")
print(f"Brown's cat is a {browns_cat.species}.")


#Instantiate another cat
garfield=Cat('Garfield',7,'Orange Cat')

garfield.sit()
garfield.purr()

print(f"That orange cat's name is {garfield.name}.")
print(f"{garfield.name} is {garfield.age} years old.")
print(f"{garfield.name} is a {garfield.species}.")