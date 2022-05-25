arr = [int(input()) for _ in range(3)]
if arr[0] == arr[1] == arr[2] == 60:
    print("Equilateral")
elif sum(arr) == 180:
    if arr[0]==arr[1] or arr[0]==arr[2] or arr[1]==arr[2]:
        print("Isosceles")
    else:
        print("Scalene")
else: print("Error")