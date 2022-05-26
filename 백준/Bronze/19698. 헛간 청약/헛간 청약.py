N,W,H,L = map(int, input().split())
d1 = W//L
d2 = H//L
print(min(N,d1*d2))