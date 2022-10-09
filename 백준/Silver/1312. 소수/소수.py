A,B,N = map(int,input().split())
level = 0

while level != N:
    level += 1
    s = (A%B)*10 # 나누기를 직접 해보면 소수점이 나올 때부터는 나누기 위해서 0이 붙음. 
    ans = s//B
    A = s

print(ans)