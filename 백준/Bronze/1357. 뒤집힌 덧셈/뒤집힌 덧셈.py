X, Y = map(int, input().split())
def Rev(X) :
    X=str(X)[::-1]
    result_list=[]
    if X[0] == "0" :
        for i in range(1, len(X)) :
            if X[i] == "0" :
                pass
            else :
                X=X[i:]
                break
        return X
    else :
        return X
final_X = int(Rev(X))
final_Y = int(Rev(Y))
final_XY = final_X + final_Y
print(Rev(final_XY))