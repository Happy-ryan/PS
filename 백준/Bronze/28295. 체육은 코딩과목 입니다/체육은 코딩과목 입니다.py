dir = ["E", "S", "W", "N"]
cur_dir = 3

for i in range(10):
    command = int(input())
    # 1 시계방향 / 2 180도 / 3 반시계방향
    # 동(0)남(1)서(2)북(3)
    if command == 1:
        cur_dir = (cur_dir + 1) % 4
    elif command == 2:
        cur_dir = (cur_dir + 2) % 4
    elif command == 3:
        cur_dir = (cur_dir - 1 + 4) % 4

print(dir[cur_dir])