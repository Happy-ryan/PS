# https://www.acmicpc.net/problem/10986

n, m = map(int, input().split())
nums = list(map(int, input().split()))

psum = [0] * (n + 1)
psum_ = [0] * (n + 1)

for i in range(n):
    psum[i + 1] = psum[i] + nums[i]
    psum_[i + 1] = (psum[i + 1]) % m

# 같은 놈(mod) - 같은 놈(mod) = 0 > m으로 반드시 나누어 떨어진다..
# 쌍 찾기 - 오른쪽을 고정하고, 찾고 싶은 왼쪽을 찾음.
# 오른쪽 기준 - 왼쪽에 나랑 같은 놈 찾기!
# 이중포문 -> 시간초과
# 해결할 필요가 있다! dic을 사용해서 누적시키기
from collections import Counter
dic = Counter()
ans = 0 
for r in range(n + 1):
    ans += dic[psum_[r]]
    dic[psum_[r]] += 1
    
    
print(ans)

# 1: [3, 3]
# 2: [1, 2], [4, 5]
# 3: [1, 3] [2, 4] [3, 5]
# 4: -
# 5: [1, 5]
# x로 끝나는 경우의 수
# 2: [1, 2]
# 3: [3, 3], [1, 3]
# 4: [2, 4]
# 5: [4, 5], [1, 5], [3, 5]