a,b = map(int, input().split())
def sum(x): # sum 함수는 x가 주어졌을 때 인덱스의 시작값을 구하는데 사용한다.
    sum = 1
    for x in range(1,x):
        sum += x
    return sum

cnt = 0
for i in range(1,47):
    for j in range(a,b+1):
        if j in range(sum(i),sum(i)+i):
            cnt += i
print(cnt)
#https://www.acmicpc.net/problem/1292
# 규칙성 찾기
# 1 idx= 1
# 2 idx=2~3
# 3 idx=4~6
# 4 idx=7~10
# 5 idx=11~15
# 6 idx=16~21
# 7 idx=22~28 
# n idx= (1+2+..n-1)~(2+3+4+...n)