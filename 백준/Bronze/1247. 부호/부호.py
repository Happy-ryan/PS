for _ in range(3):
    N = int(input())
    arr = [int(input()) for _ in range(N)]
    if sum(arr) == 0:
        print("0")
    elif sum(arr)>0:
        print("+")
    else:
        print("-")