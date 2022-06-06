a,b,c = map(int,input().split())
result1 = c -b - 1
result2 = b -a - 1
print(max(result1,result2))