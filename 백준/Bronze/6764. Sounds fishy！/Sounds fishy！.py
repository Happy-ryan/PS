arr = [int(input()) for _ in range(4)]
k = 0
for i in range(3):
    if arr[i+1] > arr[i]:
        k += 1
    elif arr[i+1] < arr[i]:
        k -= 1

if len(set(arr)) == 1: 
    print("Fish At Constant Depth")
elif k == 3:
    print("Fish Rising")
elif k == -3:    
    print("Fish Diving")
else:
    print("No Fish")