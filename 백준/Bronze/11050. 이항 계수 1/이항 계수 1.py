N, K = map(int, input().split())
def factorial(n) :
    if n ==0 or n==1 :
        return 1
    else :
        return n*factorial(n-1)

a = factorial(N)
b = factorial(K)
c = factorial(N-K)

print(a//(b*c))