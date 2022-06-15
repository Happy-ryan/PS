arr = list(map(int,input().split())) # 흰색 피스
#킹 1개, 퀸 1개, 룩 2개, 비숍 2개, 나이트 2개 폰8개 *2(검+흰)
K = 1 - arr[0]
Q = 1 - arr[1]
L = 2 - arr[2]
B = 2 - arr[3]
N = 2 - arr[4]
P = 8 - arr[5]

print(K,Q,L,B,N,P)