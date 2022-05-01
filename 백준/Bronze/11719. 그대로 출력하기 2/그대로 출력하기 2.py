#s = input() 이런 식으로 작성하면 1번밖에 입력을 받지 못한다. 입력을 지속받으려면 while,for문을 사용해야한다
# 문제는 언제 종료인지 제시가 되지 않았기 때문에 EOF를 사용해야한다. 예전에 A+B-4문제와 유사

while True :
    try :
        s = input()
        print(s)
    except EOFError :
        break   