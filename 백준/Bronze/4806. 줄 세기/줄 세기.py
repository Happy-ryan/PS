cnt = 0
while True:
    try:
        x = input()
        cnt += 1
    except EOFError:
        break
print(cnt)