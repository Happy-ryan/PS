while True:
    n = int(input())
    
    if n == -1:
        break
    
    students = []
    
    for _ in range(n):
        x, y, z, name = input().split()
        volume = int(x) * int(y) * int(z)
        students.append((volume, name))
    
    p1 = max(students)[1]
    p2 = min(students)[1]
    
    print(f"{p1} took clay from {p2}.")