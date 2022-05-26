N,M,K= map(int,input().split())
print(min(M,K)+min(N-M,N-K)) 
# 순서가 정해지기 않았기 때문에 M의 개수를 한계 생각