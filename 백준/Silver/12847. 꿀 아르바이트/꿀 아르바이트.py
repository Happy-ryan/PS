n, m = map(int, input().split())
sals = list(map(int, input().split()))

def solution(n, m, sals):
    ans = 0
    # 초기값!
    l, r = 0, m - 1
    total_sal = sum(sals[l : r + 1])
    ans = total_sal
    while True:
        # print(f"l: {l}, r: {r}, total_sal: {total_sal}, ans: {ans}")
        l += 1
        r += 1
        if l < r and r < n:
            # 그 전 것 제외
            total_sal -= sals[l - 1]
            # 새로 추가된 것 포함
            total_sal += sals[r]
            ans = max(ans, total_sal)
        else:
            return ans
        
print(solution(n, m, sals))