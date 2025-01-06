def solution(velocities):
    
    post_time = velocities[0][1]
    val = velocities[0][0] * post_time
    
    for vel, time in velocities[1:]:
        val += (time - post_time) * vel
        post_time = time
        
    return val

while True:
    t = int(input())
    if t == -1:
        break
    velocities = [list(map(int, input().split())) for _ in range(t)]
    print(f"{solution(velocities)} miles")