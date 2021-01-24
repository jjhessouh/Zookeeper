# put your python code here
three_digit_integer = int(input())

first_digit = three_digit_integer // 100
second_digit = three_digit_integer % 100 // 10
third_digit = three_digit_integer % 100 % 10

sum_of_digits = first_digit + second_digit + third_digit
print(sum_of_digits)
