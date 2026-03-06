min_temp = 100000
ans = ""

while True:
    city, temp = input().split()
    temp = int(temp)

    if temp < min_temp:
        min_temp = temp
        ans = city

    if city == "Waterloo":
        break

print(ans)