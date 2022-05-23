A,B = map(int, input().split())
set1 = set(map(int,input().split()))
set2 = set(map(int,input().split()))
set_result = set1 - set2
set_result = sorted(set_result)
if set_result == set1:
    print(0)
else:
    print(len(set_result))
    for x in set_result:
        print(x, end=" ")