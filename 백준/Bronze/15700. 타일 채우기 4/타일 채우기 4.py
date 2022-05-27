N,M = map(int,input().split())
if N%2 !=0 and M%2 !=0: #N,M 홀수
    print((N*M-1)//2)
elif N%2==0 and M%2==0: #N,M짝수
    print((N*M)//2)
else:# N OR M 짝수(홀수)
    print((N*M)//2)
