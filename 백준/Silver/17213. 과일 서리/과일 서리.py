N = int(input())
M = int(input())
# nH(m-n) = n+m-n-1Cm-n
fact = [0] * 31
fact[0] = 1
fact[1] = 1
for i in range(2,31):
    fact[i] = i * fact[i-1]
# print(fact)
p = fact[M-1]
q = fact[M-N]*fact[N-1]
print(p//q)