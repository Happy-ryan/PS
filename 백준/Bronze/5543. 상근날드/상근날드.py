arr = [int(input()) for _ in range(5)]
burger = sorted(arr[0:3])
beverage = sorted(arr[3:])
print(burger[0]+beverage[0]-50)