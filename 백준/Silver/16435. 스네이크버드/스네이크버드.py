N, L = map(int, input().split())
high = list(map(int, input().split()))
high = sorted(high)
for x in high:
    if x <= L:
        L+=1
    else :
        break
print(L)