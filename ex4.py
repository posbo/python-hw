# number of cars
cars = 100

# number of spaces
space_in_a_car = 4

# number of drivers
drivers = 30

# number of passengers
passengers = 90

#number of cars not driven
cars_not_driven = cars - drivers

# number of cars driven
cars_driven = drivers

# carpool capacity
carpool_capacity = cars_driven * space_in_a_car

# average passengers in a car
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car"

# study drills

# 1. Error on line 7, car_pool_capacity is not defined
# 2. Answer is no longer a floating point, but still correct

