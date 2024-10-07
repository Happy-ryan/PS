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
            for room in rooms:
                if len(room) == m:
                    continue
                if room[0][0] - 10 <= level <= room[0][0] + 10:
                    room.append((level, name))
                    return
            rooms.append([(level, name)])
        
        return rooms

    for player in players:
        choose_room(player)

    for room in rooms:
        print("Started!" if len(room) == m else "Waiting!")
        # 플레이어 정보 닉네임 사전순 출력
        room.sort(key=lambda x :x[1])
        for row in room:
            print(*row)
            
solution(p, m, players)