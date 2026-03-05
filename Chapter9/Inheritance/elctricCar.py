#setting default value for an Attribute
class Car:
    """A simple attempt too represent a car"""
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odomoter_reading = 0
        
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name ."""

        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a  statement showing the car's mileage"""
        print(f"This car has {self.odomoter_reading} miles on it.")

    def update_odometer(self,mileage):
        """Set the odometer readinng to the given value."""
        if mileage>=self.odomoter_reading:
            self.odomoter_reading = mileage
        else:
            print(f"You can't roll back an odometer")
    def increment_odometer(self,miles):
        """Add the given amount to the odomoter reading."""
        self.odomoter_reading+=miles    
    def fill_gas_tank(self):
        print("fill the tank homie")

## the battery class
class Battery:
    """A simple atttempt to model a battery for an electric car"""
    def __init__(self,battery_size =40):
        """Initialize the battery's attricbutes."""
        self.battery_size = battery_size
    def describe_battery(self):
        """Print a statement describing the battery size"""
        print(f"This car has a {self.battery_size}-kwh battery")

    def get_range(self):
        """Print a statement about the range this battery provides """
        if self.battery_size ==40:
            range = 150
        elif self.battery_size ==65:
            range =25
        print(f"This car can go about {range} miles on a full charge ")
    def upgrade_battery(self):
        if self.battery_size !=65:
            self.battery_size =65
        
    
class ElectricCar(Car):
    """Represent aspects of a car , specific to electric vehicles"""
    def __init__(self,make,model,year):
        """Initialize attributes of the parent class"""
        super().__init__(make,model,year) #parent -super child -subclass
        self.battery =Battery()
    
    #     self.battery_size = 30
    # def describe_battery(self):
    #     """Print a statement describing the battery size"""
    #     print(f"This car has  a battery size of {self.battery_size}-kwh ")
    
    def fill_gas_tank(self):
        """Electric cars dont have a tank homie"""
        print("This car doesnn't have a gas tank")



    
# vayu = ElectricCar("Tesla",'Model S','2025')
# print(vayu.get_descriptive_name())
# vayu.describe_battery()
# vayu.fill_gas_tank()

#You can break your large class into smaller
# classes that work together; this approach is called compositio


    
vayu = ElectricCar("Tesla",'Model S','2025')
vayu.battery.get_range()
vayu.battery.upgrade_battery()
vayu.battery.get_range()



