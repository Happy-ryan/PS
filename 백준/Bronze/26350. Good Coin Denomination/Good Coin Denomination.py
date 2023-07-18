def check(arr):
    flag = True
    for i in range(1, len(arr) - 1):
        if arr[i] * 2 > arr[i + 1]:
            flag = False
    return flag
    
    
def f(arr):
	ans = ""
	for x in arr[1:]:
		ans += str(x) + " "
	return ans

t = int(input())
for _ in range(t):
    arr = list(map(int, input().split()))
    print(f"Denominations: {f(arr)}")
    if check(arr):
        print("Good coin denominations!")
    else:
        print("Bad coin denominations!")
    print()
        
    # your code goes here