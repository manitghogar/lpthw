#assigning a number to cars
cars = 100
#defining how many seats available in a car
space_in_a_car = 4.0
#how many drivers out there
drivers = 30
#how many passengers out there
passengers = 90
#equation for cars that are not driven
cars_not_driven = cars - drivers
#equation for cars that are driven
cars_driven = drivers
#total current capacity for carpool
carpool_capacity = cars_driven * space_in_a_car
#how many passengers can a car have on average
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."

print "There are only", drivers, "drivers available."

print "There will be", cars_not_driven, "empty cars today."

print "We can transport", carpool_capacity, "people today."

print "We have", passengers, "to carpool today."

print "We need to put about", average_passengers_per_car, "in each car."

"""Study Drill 0: NameError: name 'car_pool_capacity' is not defined. This error suggests that one of the 
varilables (car_pool_capacity) is not defined, therefore the program will not run."""

"""Study Drill 1: If space_in_a_car is = 4 and not 4.0, then the 120 is outputed not as a floating point number"""