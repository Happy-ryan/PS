# # https://www.acmicpc.net/problem/2023
# # 소수 구하기
def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def dfs(cur, level, n):
    if not isPrime(cur):
        return
    if level == n:
        print(cur)
        return
    # 1부터 시작
    for num in range(1, 10):
        dfs(cur * 10 + num, level + 1, n)

# cur 현재 가장 왼쪽의 위치에 해당함.
# 0과 1은 가장 왼쪽에 올 수 있는 숫자에 해당하지 않음.
# cur = 0만 넣으면 당연히 dfs 진행 X
# cur를 2부터 9까지 전부 살펴봐야함.
n = int(input())
for cur in range(2, 10):
    level = 1
    dfs(cur, level, n)