n = int(input())
arr=set()
for _ in range(n):
    s = input().split()
    if s[1]=="enter":
        arr.add(s[0]) #set함수에서 특정요소 추가하기
    else: # s[1]=="leave" 인 경우
        arr.remove(s[0]) #set함수에서 특정요소 제거하기. 인덱스를 파악안해도 되기 때문에 훨씬 빠르다.
arr = sorted(arr)[::-1]
print(*arr, sep="\n")
