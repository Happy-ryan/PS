import sys
input = sys.stdin.readline

N = int(input())
participants = []

for i in range(1, N + 1):
    S, C, L = map(int, input().split())
    # 정렬 기준에 맞게 튜플 구성
    participants.append((-S, C, L, i))
    # 점수는 클수록 좋으므로 -S

# 정렬
participants.sort()

print(participants[0][3])
