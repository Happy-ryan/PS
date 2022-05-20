N = int(input())
M = int(input())
arr=set(map(int, input().split()))
cnt = 0
for x in arr :
    if M-x in arr:
        cnt +=1
print(cnt//2)