# https://www.acmicpc.net/problem/25285


def bmi(tall, weight):
    return (weight / tall**2) * 10000


def check(tall, weight):
    bmi_ = bmi(tall,weight)
    if tall < 140.1:
        return 6
    elif tall < 146:
        return 5
    elif tall < 159:
        return 4
    elif tall < 161:
        if bmi_ >= 16 and bmi_ < 35:
            return 3
        else:
            return 4
    elif tall < 204:
        if bmi_ >= 20 and bmi_ < 25:
            return 1
        elif (18.5 <= bmi_ < 20.0) or (25 <= bmi_ < 30):
            return 2
        elif (16 <= bmi_ < 18.5) or (30 <= bmi_ < 35):
            return 3
        elif bmi_ < 16 or bmi_ >= 35:
            return 4
    else:
        return 4
    
    
t = int(input())
for _ in range(t):
    tall, weight = map(int, input().split())
    print(check(tall, weight))