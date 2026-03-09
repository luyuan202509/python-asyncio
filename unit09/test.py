
class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        print("The restaurant name is " + self.restaurant_name.title() + ".")
        print("The restaurant type is " + self.cuisine_type.title() + ".") 

    def open_restaurant(self):
        print("The restaurant is open.")

    def set_number_served(self,number_served):
        if number_served >= 0:
            self.number_served = number_served
        else:
            print("The number of served can't be negative.")
    
    def increment_number_served(self,number_served):
        if number_served >= 0:
            self.number_served += number_served
        else:
            print("The number of served can't be negative.")





if __name__ == '__main__':

    restaurant = Restaurant('Shuicheng Bake Fish','fish')
    restaurant.describe_restaurant()
    restaurant.open_restaurant()