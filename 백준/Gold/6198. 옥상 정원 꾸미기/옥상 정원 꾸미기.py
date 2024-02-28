# 한 방향을 바라봐서 가장 큰 값을 찾는 문제
# 오큰수, 탑, 옥상정원꾸미기

n = int(input())
highs = [int(input()) for _ in range(n)]
# 내 오른쪽에 나보다 작은 높이는 필요없어!
# 뒤에서부터 넣을거야!
def solution(n, highs):
    stack = []
    # 왼쪽에 나보다 작은값 있으면 안돼
    # 실제로는 1(0) 4(1) 7(2) 9 
    # 9의 입장에서는 3개를 볼 수 있는데 7의 왼쪽에는 1, 4가 살아남을 수 없어서
    # 9의 입장에서는 현재 스택에서 7만 볼 수 있다.
    # 따라서 7 높이에서 볼 수 있는 건물의 수 + 7건물 자체(+1)
    memo = [0 for _ in range(n)]
    for idx, high in enumerate(highs[::-1]):
        cnt = 0
        while stack and stack[-1][1] < high:
            exit_idx, _ = stack.pop()
            # 
            cnt += max(memo[exit_idx] + 1, 1)
            
        memo[idx] = cnt
            
        stack.append((idx,high))
        
    return sum(memo)

print(solution(n, highs))