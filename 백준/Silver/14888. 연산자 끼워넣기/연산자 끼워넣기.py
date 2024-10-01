n = int(input())
nums = list(map(int, input().split()))
cmds = list(map(int, input().split()))

def solution(n, nums, cmds):
    global res, max_ans, min_ans
    
    # 더하기 / 빼기 / 곱하기 / 나누기
    # dfs 돌면서 갱신...더하기 -> 다시 원복..이런 식이 되지 않을까
    inf = int(1e18)
    
    max_ans = -inf
    min_ans = inf
    
    res = nums[0]
    def dfs(idx):
        global res, max_ans, min_ans
        # 주어진 연산을 모두 사용했을 때만 갱신
        if sum(cmds) == 0:
            max_ans = max(max_ans, res)
            min_ans = min(min_ans, res)
        for k in range(4):
            # 더하기
            if k == 0 and cmds[k] > 0:
                cmds[k] -= 1
                res += nums[idx]
                dfs(idx + 1)
                res -= nums[idx]
                cmds[k] += 1
            # 빼기
            if k == 1 and cmds[k] > 0:
                cmds[k] -= 1
                res -= nums[idx]
                dfs(idx + 1)
                res += nums[idx]
                cmds[k] += 1
            # 곱하기
            if k == 2 and cmds[k] > 0:
                cmds[k] -= 1
                res *= nums[idx]
                dfs(idx + 1)
                res //= nums[idx]
                cmds[k] += 1
            # 나누기
            if k == 3 and cmds[k] > 0:
                # 원상복귀용 > 
                tmp = res
                cmds[k] -= 1
                if res < 0:
                    res *= -1
                    res //= nums[idx]
                    res *= -1
                else:
                    res //= nums[idx]
                dfs(idx + 1)
                res = tmp
                cmds[k] += 1
                
        return max_ans, min_ans

    dfs(1)
    
    print(max_ans)
    print(min_ans)

solution(n, nums, cmds)