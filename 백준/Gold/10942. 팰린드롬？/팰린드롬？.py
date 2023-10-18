# https://www.acmicpc.net/problem/10942
# 팰린드롬
# E - S = 0 이면 구간의길이는 1로 반드시 팰린드롬
# E - S = 1 이면 구간의 길이는 2로 두 숫자가 같아야 팰린드롬
# E - s >= 2 이면 구간의 길이는 3이상으로 양 끝의 숫자가 같고 양 끝을 제외한 숫자도 팰린드롬이어야한다. ex) 5 팰린드롬 5 (0) // 1 팰린드롬 5(X) // 5 팰린드롬(X) 5(X)
import sys
input = sys.stdin.readline

def isPalindrom(row: list):
    n = len(row)
    # 2차원 dp로 S, E을 인덱스로 기록할 것.
    # dp의 정의: dp[s][e] 는 row[s:e+1]이 팰린드롬인가 확인
    dp = [[0 for _ in range(n)] for _ in range(n)]
    # E - S = 0인 경우
    for s in range(n):
        for e in range(n):
            if s == e:
                dp[s][e] = 1
    # E - S = 1인 경우
    for s in range(n):
        for e in range(n):
            if e - s == 1 and row[s] == row[e]:
                dp[s][e] = 1
    # E - S >= 2인 경우
    # 5 1 2 1 5 (0)
    # s [s+1 ~ e-1] e
    for s in reversed(range(n)):
        for e in range(s + 2, n):
            if e - s >= 2 and row[s] == row[e] and dp[s + 1][e - 1]:
                dp[s][e] = 1
                
    return dp

n = int(input())
row = list(map(int, input().split()))
dp = isPalindrom(row)
m = int(input())
for _ in range(m):
    # 1base
    s, e = map(int, input().split())
    s -= 1
    e -= 1
    print(dp[s][e])
