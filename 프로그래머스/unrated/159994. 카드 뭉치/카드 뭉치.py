def solution(cards1, cards2, goal):
    flag = True
    while len(goal) != 0:
        if goal[0] in cards1:
            if goal[0] == cards1[0]:
                goal.pop(0)
                cards1.pop(0)
            else:
                flag = False
                break
        else:
            if goal[0] == cards2[0]:
                goal.pop(0)
                cards2.pop(0)
            else:
                flag = False
                break
    if flag:
        return 'Yes'
    else:
        return 'No'
                
    

