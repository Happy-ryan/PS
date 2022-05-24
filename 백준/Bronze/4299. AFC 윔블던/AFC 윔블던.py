hap,tea = map(int,input().split())
if hap<tea  or ((hap+tea)%2 != 0):
    print(-1)
else:
    case1 = (hap+tea)//2
    case2 = hap-case1
    if case1>case2:
        print(case1,case2)
    else: print(case2,case1)


