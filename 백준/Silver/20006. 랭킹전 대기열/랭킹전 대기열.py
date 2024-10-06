p, m = map(int, input().split())
players = [list(input().split()) for _ in range(p)]

def solution(p, m, players):
    rooms = []

    def choose_room(player):
        level, name = player 
        level = int(level)
        # 방이 하나도 없다면 생성
        if not rooms:
            rooms.append([(level, name)])
        else:
            # 방은 있는데..어디로 들어갈까?
            check = []
            for idx, room in enumerate(rooms):
                check.append((idx, room[0][0]))
            
            inf = int(1e18)
            flag = inf
            for (idx, standard) in check:
                if len(rooms[idx]) < m and standard - 10 <= level and level <= standard + 10:
                    flag = idx
                    break # 모든 방에 들어갈 수 있다면 가장 먼저 생성된 방에 들어가야함. 그래서 찾으면 멈추기
                    
            if flag == inf:
                rooms.append([(level, name)])
            else:
                rooms[idx].append((level, name))

    for player in players:
        choose_room(player)

    for room in rooms:
        print("Started!" if len(room) == m else "Waiting!")
        # 플레이어 정보 닉네임 사전순 출력
        room.sort(key=lambda x :x[1])
        for row in room:
            print(*row)
            
solution(p, m, players)