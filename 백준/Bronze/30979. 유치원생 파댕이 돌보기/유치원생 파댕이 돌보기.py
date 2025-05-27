t = int(input())
n = int(input())
Fs = list(map(int, input().split()))

print('Padaeng_i Happy' if sum(Fs) >= t else 'Padaeng_i Cry')