#9-1 Restaurant
class Restaurant:
    
    def __init__(self,restaurant_name,cuisine_type,number_served=0):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        self.number_served=number_served
    
    def describe_restaurant(self):
        print(f"The restaurant: {self.restaurant_name} offers {self.cuisine_type}.")
        
    def open_restaurant(self):
        print(f"{self.restaurant_name} is officially open!")
        
    def set_number_served(self,number: int):
        self.number_served=number
        return self.number_served
        
    def increment_number_served(self,number):
        self.number_served+=number
        return self.number_served