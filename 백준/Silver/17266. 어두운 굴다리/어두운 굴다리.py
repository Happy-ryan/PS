n = int(input()) # 굴다리 길이
m = int(input()) # 가로수의 개수
lights = list(map(int, input().split())) # 가로등의 위치

def solution(n, m, lights):
    
    # 가로등 1개 & 양 끝..굴다리 길이만큼 높아야함
    # 가로등 1개 & 가운데 쯤..굴다리 길이 / 2 정도 높아야함..

    # h -> N
    # c -> right - left -> N
    # O(N^2) -> 시간초과
    
    # 특정 높이일 때 가로등이 굴다리를 커버할 수 있는가 판단하는 함수
    # 시간복잡도 N
    # 칸이냐 선이냐 하나로 잘 정해야함,,,
    def f(h):
        last = 0
        check = [0] * (n)
        for l in lights:
            left = max(last, l - h)
            right = min(n, l + h) - 1 # 난 칸으로 봄
            for c in range(left, right + 1):
                if check[c] == 0:
                    check[c] = 1
            last = right
        if check.count(1) == len(check):
            return True
        return False
    
    # 정답 : 오른쪽을 봄 -> 왼쪽 출력 (역전)
    # 역전될때까지 : l > r 되어야함! --> l <'=' r : = 들어간 이유
    l, r = 1, int(1e5) + 1 # 높이를 의미함.
    while l <= r:
        m = (l + r) // 2
        # print(f"l: {l}, r: {r}, m: {m}, {f(m)}")
        if f(m):
            r = m - 1
        else:
            l = m + 1

    return l
        
    
print(solution(n, m, lights))
