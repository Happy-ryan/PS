K = int(input())
for i in range(1,K+1) :
    gap_list =[]
    arr = list(map(int, input().split()))[1:]
    arr_sort = sorted(arr)
    for j in range(len(arr)-1) :
        gap = arr_sort[j+1]-arr_sort[j]
        gap_list.append(gap)
    print(f"Class {i}")
    print(f"Max {max(arr)}, Min {min(arr)}, Largest gap {max(gap_list)}")
