go = True

while go:
    kg = float(input())
    if kg < 0:
        go = False
    else:
        ans = kg*0.167
        res = f"Objects weighing {kg:.2f} on Earth will weigh {ans:.2f} on the moon."
        print(res)