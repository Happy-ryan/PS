a = input()
b = input()

res = ''

for a_, b_ in zip(a, b):
    if int(a_) >= int(b_):
        res += a_
    else:
        res += b_

print(res)