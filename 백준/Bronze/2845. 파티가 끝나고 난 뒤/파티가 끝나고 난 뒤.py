L,P = map(int,input().split())
people = list(map(int, input().split()))
total_people = L*P  
for x in people:
    print(x-total_people, end=" ")