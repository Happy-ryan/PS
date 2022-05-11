N = int(input())
arr = [ int(input()) for _ in range(N)]
cutline = 0 # 커트라인보다 작거나 같으면 보이지 않는 다는 것을 이용할 계획
cnt = 0
for h in reversed(arr):
    if h <= cutline :
        continue
    else : 
        cutline = h
        cnt +=1
print(cnt)