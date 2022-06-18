import math
n1, n2, n12 = map(int,input().split())
N = ((n1+1)*(n2+1)/(n12+1))-1
print(math.floor(N))
#'{:2f}'.format(N) N을 소수 세 번째에서 반올림