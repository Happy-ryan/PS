#조건 : 게임 완벽하게 진행 - 덜도 더도 딱 정량 만큼
# 홀수 5 = 상근 1 + 창영 3  상근 1 
#       = 상근 1 + 창영 1 + 상근 3
#       = 상근 3 + 창영 2 (발생 불가) : 상근이는 절대 3을 선택하지 않을 것
#       > 1개를 선택하면 무조건 내가 이기는데 굳이? 3을 선택한다.
# 짝수 6 = 상근3 + 창영
#       = 상근 1 + 창영 1 + 상근 1 + 창영 3
#       = 상근 1 + 창영3 + 상근 2 ( 완벽x)  


N = int(input())
if N % 2 != 0:
    print('SK')
else:
    print('CY')