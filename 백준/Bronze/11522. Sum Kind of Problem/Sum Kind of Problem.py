t = int(input())
for _ in range(t):
    k, N = map(int, input().split())
    S1 = N*(N+1)//2
    S2 = int((N*2)*(N/2))
    S3 = int((N*2+2)*(N/2))
    print(k, S1, S2, S3)