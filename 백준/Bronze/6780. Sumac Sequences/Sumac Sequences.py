t1 = int(input())
t2 = int(input())

ans = [t1, t2]

while True:
    if ans[-1] > ans[-2]:
        print(len(ans))
        break
    ans.append(ans[-2] - ans[-1])
    
# 120 58 62 