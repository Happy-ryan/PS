N, K= map(int, input().split())
# # for _ in range(N) :
# #     n = int(input())
arr=[int(input()) for _ in range(N)] #리스트컴프리헨션써도 입력이 세로로 들어간다. for문 고집 안해도 된다.
# arr = [802, 743,457,539]
def len_num(x): # arr에 있는 랜선의 길이를 모두 동일한 길이(x)로 자르는 후 랜선의 개수 의미
    num = 0
    for y in arr:
        num += y//x
    return num         ## len_num(x) = f(x) 가 단순하다.
# print(len_num(1)) # x로 잘랐을 때 랜선의 개수이다.186~200까지는 11개 1은 2541개 계단식하향 그래프 발생
                    # 직접 대입해보면 계단식 하향 그래프가 f(X)의 그래프이다.
l,r = 1,2**31    #l과r은 동일하게 나눌 랜선의 길이
while r-l != 1:
    m = (r+l)//2
    if len_num(m) >= K:
        l = m
    else : r=m
print(l)