X, Y = map(int, input().split())
original_Z = (Y*100)// X
def f(plus): # 게임의 횟수 추가에 따른 이길 확률 계산 > x의 의미 : 추가되는 게임의 횟수
    Z = ((Y+plus)*100)//(X+plus)
    return Z
#print(f(6)) # 6회의 게임을 추가했다.
l,r = Y , int(1e15)
if f(int(1e15)) == original_Z : # 47/47 이나 99/100과 같은 경우는 original_Z에서 벗어나지 못한다.
    print(-1)
else :
    while r - l != 1:  
        m =(r+l)//2
        if  f(m-Y) >original_Z : # f(plus): 추가되는 횟수이므로 m-Y해야한다.
            r =m
        else: l=m
    print(r-Y)