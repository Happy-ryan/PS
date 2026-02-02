n, c = map(int, input().split())
infos = [list(input().split()) for _ in range(n)]

total_area_all, total_area_bed, cost_flat = 0, 0, 0

for info in infos:
    a, name = info
    
    a = int(a)

    total_area_all += a
    
    cost_flat += a * c
    
    if name == 'bedroom':
        total_area_bed += a
    
    if name == 'balcony':
        cost_flat -= a * c * 0.5
        

print(total_area_all)
print(total_area_bed)
print(cost_flat)