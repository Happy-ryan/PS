# https://www.acmicpc.net/problem/17176
from collections import defaultdict, Counter

alphas = "abcdefghijklmnopqrstuvwxyz"

private_key = defaultdict()
private_key[0] = " "
for alpha in alphas:
    upper_alpha = alpha.upper()
    private_key[ord(upper_alpha) - 64] = upper_alpha
    private_key[ord(alpha) - 70] = alpha

n = int(input())
public_keys = list(map(int, input().split()))
ans = ""
for k in public_keys:
    ans += private_key[k]
    
t = Counter(sorted(list(input())))
ans = Counter(sorted(list(ans)))

if ans == t:
    print("y")
else:
    print("n")