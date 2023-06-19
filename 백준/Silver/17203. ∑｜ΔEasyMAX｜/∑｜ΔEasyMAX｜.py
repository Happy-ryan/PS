# https://www.acmicpc.net/problem/17203
# 누적합 미사용시 시간복잡도 O(N^2*Q) = 1000 * 1000 * 1000 = 10^9
# 시간복잡도 고려 > 누적합 > O(N * Q) = 1000 * 1000

def solution(arr:list, queries: list[list[int, int]]):
    # 1base - 누적합
    psum = [0] * len(arr)
    for i in range(len(arr) - 1):
        psum[i + 1] = psum[i] + abs((arr[i + 1] - arr[i]))

    for query in queries:
        print(abs(psum[query[0]-1] - psum[query[-1]-1]))
            
n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [list(map(int, input().split())) for _ in range(m)]
solution(arr, queries)