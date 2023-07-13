money = int(input())

if money * 0.01 + 25 < 100:
    print(100)
elif money * 0.01 + 25 > 2000:
    print(2000)
else:
    print(money * 0.01 + 25)