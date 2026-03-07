n = int(input())
iphones = list(map(int, input().split()))

status = 0
battery = 0
base = 2

for number in iphones:
    
    if status == number:
        base *= 2
    else:
        base = 2
    
    battery += base
    
    if battery >= 100:
        battery = 0
        base = 2
        status = 0
        continue
    
    status = number

print(battery)