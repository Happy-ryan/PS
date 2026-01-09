A, B, C, D = map(int, input().split())

shuttle_ok = (A + B) <= D
walk_ok = C <= D

if shuttle_ok and walk_ok:
    print("~.~")
elif not shuttle_ok and not walk_ok:
    print("T.T")
elif shuttle_ok:
    print("Shuttle")
else:
    print("Walk")