n = int(input())

# 리스트 안의 원소들 곱하는 함수
def multi_list(list):
    cnt = 1
    for x in list:
        cnt *=x
    return cnt

if n < 10:
    print('NO')
else:
    s = 0
    arr = list(map(int,str(n)))
    result = set()
    for _ in range(len(arr)-1):
        mul1 = arr[:s+1]
        mul2 = arr[s+1:]
        # print(mul1,mul2)
        # result.add(multi_list(mul1))
        # result.add(multi_list(mul2))
        if multi_list(mul1) == multi_list(mul2):
            result.add('YES')
        else: pass
        s +=1
    if "YES" in result:
        print("YES")
    else: print("NO")