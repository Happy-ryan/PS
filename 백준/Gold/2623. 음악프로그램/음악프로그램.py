# https://www.acmicpc.net/problem/2623
n, m = map(int, input().split())
adj = [[] for _ in range(n + 1)]
ind = [0 for _ in range(n + 1)]

for _ in range(m):
    nums = list(map(int, input().split()))
    for i in range(1, nums[0]):
        # 그래프 생성 - 방향성 존재
        adj[nums[i]].append(nums[i + 1])
        # 진입하는 경우 in-degree 증가
        ind[nums[i + 1]] += 1

# in-degree = 0 후보군 넣기
candidates = []
for i in range(1, n + 1):
    if ind[i] == 0:
        candidates.append(i)

result = []
while candidates:
    # 후보군에서 추출
    cur = candidates.pop()
    result.append(cur)
    # 추출 후 연결된 다음 노드들의 in-degree 제거
    for nxt in adj[cur]:
        ind[nxt] -= 1
        if ind[nxt] == 0:
            candidates.append(nxt)

if len(result) != n:
    print(0)
else:
    for num in result:
        print(num)