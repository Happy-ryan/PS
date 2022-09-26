x,y = map(int,input().split())
d_mon = {0:'SUN',1:'MON',2:'TUE',3:'WED',
        4:'THU',5:'FRI',6:'SAT'}
d_tue = {6:'SUN',0:'MON',1:'TUE',2:'WED',
        3:'THU',4:'FRI',5:'SAT'}
d_wed = {5:'SUN',6:'MON',0:'TUE',1:'WED',
        2:'THU',3:'FRI',4:'SAT'}
d_thu = {4:'SUN',5:'MON',6:'TUE',0:'WED',
        1:'THU',2:'FRI',3:'SAT'}
d_fri = {3:'SUN',4:'MON',5:'TUE',6:'WED',
        0:'THU',1:'FRI',2:'SAT'}
d_sat = {2:'SUN',3:'MON',4:'TUE',5:'WED',
        6:'THU',0:'FRI',1:'SAT'}
d_sun = {1:'SUN',2:'MON',3:'TUE',4:'WED',
        5:'THU',6:'FRI',0:'SAT'}
# 1(mon) > +3 > 2(thu) > +0 > 3(thu) > +3 > 4(sun)
# > +2 > 5(tue) > +3 > 6(fri) > +2 > 7(sun) > +3 > 8(wed)
# > +3 > 9(sat) > +2 > 10(mon) > +3 > 11(thu) > +2 > 12(sat)
if x == 1:
    res = y%7
    print(d_mon[res])
elif x == 2:
    res = y%7
    print(d_thu[res])
elif x == 3:
    res = y%7
    print(d_thu[res])
elif x == 4:
    res = y%7
    print(d_sun[res])
elif x == 5:
    res = y%7
    print(d_tue[res])
elif x == 6:
    res = y%7
    print(d_fri[res])
elif x == 7:
    res = y%7
    print(d_sun[res])
elif x == 8:
    res = y%7
    print(d_wed[res])
elif x == 9:
    res = y%7
    print(d_sat[res])
elif x == 10:
    res = y%7
    print(d_mon[res])
elif x == 11:
    res = y%7
    print(d_thu[res])
else:
    res = y%7
    print(d_sat[res])