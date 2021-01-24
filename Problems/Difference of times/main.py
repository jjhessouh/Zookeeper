# put your python code here


hour_1 = int(input())
min_1 = int(input())
sec_1 = int(input())

time_1 = (hour_1 * 60 * 60) + (min_1 * 60) + sec_1

hour_2 = int(input())
min_2 = int(input())
sec_2 = int(input())

time_2 = (hour_2 * 60 * 60) + (min_2 * 60) + sec_2

difference_between_time = time_2 - time_1
print(difference_between_time)



