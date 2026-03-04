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

    def set_odometer(self,mileage):
        """Set the odometer readinng to the given value."""
        self.odomoter_reading = mileage
my_new_car = Car('audi','a4',2024)

print(my_new_car.get_descriptive_name())
# my_new_car.odomoter_reading=123
my_new_car.set_odometer(12312)
my_new_car.read_odometer()

