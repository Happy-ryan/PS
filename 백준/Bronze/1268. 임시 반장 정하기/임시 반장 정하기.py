N = int(input())
graph = [ list(map(int,input().split())) for row in range(N)]
graph_rev = []

for c in range(5):
    arr = []
    for r in range(N):
        arr.append(graph[r][c])
    graph_rev.append(arr)

# print(graph_rev)

num_class = {}
for x in range(N):
    ans = []  # 1번 학생 기준 = 학생을 기준점으로
    for row in graph_rev:
        for y in range(N):
            if x != y and row[x] == row[y]:
                if y not in ans:
                    ans.append(y)
    num_class[x+1] = len(ans)

# print(num_class)
# print(list(num_class.items()))
max_v = max(num_class.values())
ans = set()
for k,v in list(num_class.items()):
    if max_v == v:
        ans.add(k)
print(min(ans))