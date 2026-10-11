import math
def calculate_trip_cost(distance, fuel_consumption, fuel_price):
    fuel_needed = distance / 100 * fuel_consumption
    cost = fuel_needed * fuel_price
    return math.ceil(cost)

print(calculate_trip_cost(200, 5, 50))