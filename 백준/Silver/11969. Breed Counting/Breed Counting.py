# https://www.acmicpc.net/problem/11969
# 시간복잡도: 이중for문 > O(N^2*Q) = 10^15
# 특정 구간에서의 정보 -> 누적합의 관점에서 접근해보자.
# 누적합을 안쓰더라도 Counter로 충분해보임

def solution(arr:list, qs:list[list[int, int]]):
    # 1, 2, 3의 등장횟수를 누적해서 저장함 > 그 전 리스트의 값 가져옴 > copy 활용
    # 새로운 등장하는 숫자 추가 > 1base이므로 [0, 0, 0, 0]로 설정
    psum = [[0, 0, 0, 0] for _ in  range((len(arr) + 1))]
    for i in range(len(arr)):
        psum[i+1] = psum[i].copy()
        psum[i + 1][arr[i]] += 1
        
    for q in qs:
        s, e = q
        for j in range(1, 4):
            print(psum[e][j] - psum[s - 1][j], end=" ")
        print()
    
    
    
n, q = map(int, input().split())
arr = [int(input()) for _ in range(n)]
qs = [list(map(int, input().split())) for _ in range(q)]
solution(arr, qs)