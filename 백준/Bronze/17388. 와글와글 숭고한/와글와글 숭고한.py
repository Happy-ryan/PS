arr = list(map(int, input().split()))
if sum(arr) >= 100:
    print("OK")
else :
    if arr.index(min(arr)) == 0:
        print("Soongsil")
    elif arr.index(min(arr)) ==1:
        print("Korea")
    else: print("Hanyang")