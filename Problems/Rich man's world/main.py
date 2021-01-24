deposit = int(input())
y = 0
while deposit <= 700000:
    deposit = deposit * (1 + 7.1 * 1 / 100)
    y += 1
print(y)