t = int(input())

def solution(heights):
    arr = []
    
    # is_over = False
    cnt = 0
    for height in heights:
        if not arr:
            arr.append(height)
        else:
            new_arr = []
            is_over = False
            for idx, h in enumerate(arr):
                if h > height:
                    is_over = True
                    new_arr += arr[:idx]
                    new_arr.append(height)
                    new_arr += arr[idx:]
                    cnt += len(arr) - idx
                    break
            if not is_over:
                new_arr = arr[:]
                new_arr.append(height)
            
            arr = new_arr[:]
            
        # print(f"투입: {height}")
        # print(f"{arr}")
        # print(f"걸음수 :{cnt}")
        # print("=")

    return cnt


for _ in range(t):
    arr = list(map(int, input().split()))
    case = arr[0]
    heights = arr[1:]
    print(f"{case} {solution(heights)}")