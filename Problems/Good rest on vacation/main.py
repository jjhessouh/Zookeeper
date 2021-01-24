# put your python code here

duration_in_days = int(input())
food_cost_day = int(input())
flight_cost = int(input())
hotel_night_cost = int(input())

number_of_night = duration_in_days - 1

total_required_sum = (duration_in_days * food_cost_day) + (flight_cost * 2) + (hotel_night_cost * number_of_night)
print(total_required_sum)