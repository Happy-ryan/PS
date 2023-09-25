from collections import deque

n, k = map(int, input().split())
health = deque(map(int, input().split()))
robots = deque([False] * n)

def getout():
    if robots[-1]:
        robots[-1] = False

t = 0
while True:
    t += 1
    # 1. 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전한다.
    health.rotate(1)
    robots.rotate(1)
    getout()
    
    # 2. 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다. 만약 이동할 수 없다면 가만히 있는다.
    for i in range(n-2, -1, -1):
        # 1) 로봇이 이동하기 위해서는 이동하려는 칸에 로봇이 없으며, 그 칸의 내구도가 1 이상 남아 있어야 한다.
        # 오래된 로봇 - 먼저 올린 로봇 - 인덱스 큰 로봇 부터 확인해야함. range에서 반대로 체크하는 이유
        # i칸에 로봇이 존재 & i + 1 칸에 로봇이 없음 & i + 1 칸에 내구도가 존재 -> 이동가능
        # i칸에 있던 로봇이 i+1칸으로 이동하면 기존의 i칸은 False로 변경
        # 벨트가 회전하든 로봇이 이동하든 '내리는 곳'에 위치하면 즉시 내려가기 때문에 로봇의 위치가 변경했을 때 확인해야함.getout
        if robots[i] and not robots[i+1] and health[i+1] > 0:
            robots[i+1] = True
            robots[i] = False
            health[i+1] -= 1
        getout()
        
    # 3. 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.
    if health[0] > 0:
        robots[0] = True
        health[0] -= 1

    # 4. 내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료한다. 그렇지 않다면 1번으로 돌아간다
    if health.count(0) >= k:
        break
print(t)
