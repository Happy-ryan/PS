phones = list(input().split())
prefix = input()
cnt = 0
k = len(prefix)
for phone in phones:
    if phone[:k] == prefix and len(phone[:k +1]) > len(prefix):
        cnt += 1
print(cnt)