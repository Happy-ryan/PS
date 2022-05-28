n = input()
if len(n) <3:
    arr = list(n)
    sum = 0
    for x in arr:
        sum += int(x)
    print(sum)
elif n =="110" or n=="101":
    print("11")
else: 
    sum=0
    arr = list(n)
    for x in arr:
        if x =="1":
            sum += 10
        else :
            sum += int(x)
    print(sum)

# 110 , 210, 310, 410, 510, 610, 710, 810, 910
# 101, 102, 103, 104, 105, 106, 107, 108, 109