s = input()
for i in s:
    if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        result = i.lower()
    else: result = i.upper()
    print(result,end="")