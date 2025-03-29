n = int(input())
arr = list(range(1, n + 1))

def AB():
    new_arr = []
    for idx, x in enumerate(arr):
        if idx % 2 != 0:
            new_arr.append(x)
    return new_arr

while True:
    if len(arr) == 1:
        print(arr[0])
        break
    # print(f"변경 전 : {arr}")
    arr = AB()
    # print(f"변경 후 : {arr}")