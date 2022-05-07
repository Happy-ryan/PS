N=int(input())
arr=list(map(int, input().split()))
M=int(input())
# 지방의 요구예산의 합 > 국가 총 예산 일 때 max상한선 찾아라.
# 지방의 요구예산의 합 <= 국가 총 예산 일 때 max지방 요규예산 찾아라.
if sum(arr) <= M :
    print(max(arr))
else :
    def f(x): #상한선x가 존재할 때 지방 요구 예산의 총합    
        sum = 0
        for i in arr:
            if x >= i:
                sum += i
            else : 
                sum += x
        return sum
    l,r =0 ,max(arr)  # r과l은 예산안의 상한을 의미한다. # r의 범위:1 ~ max(arr) 반드시 상한이 존재하는 케이스 이므로 r의 최솟값을 정수 최소 상한 1이다. 
    while r-l != 1:
        m=(r+l)//2
        if f(m) <= M:
           l = m
        else : r=m

    print(l)