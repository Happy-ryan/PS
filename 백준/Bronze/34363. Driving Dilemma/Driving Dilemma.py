S = int(input())
D = float(input())
T = float(input())

speed_fps = S * 5280 / 3600
distance_travelled = speed_fps * T

if distance_travelled >= D:
    print("MADE IT")
else:
    print("FAILED TEST")
