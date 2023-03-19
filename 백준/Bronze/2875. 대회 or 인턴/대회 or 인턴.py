# https://www.acmicpc.net/problem/2875
# 인턴쉽 참가자들 생각하지말고 만들 수 있는 최대 팀의 개수 파악
# 최대 팀의 개수 파악 후 인턴쉽 보낼 사람 파악
# 팀을 만들고 남은 사람의 수가 인턴쉽 필수 인원보다 많으면 최대 팀 그래도 출력
# 팀을 만들고 남은 사람의 수가 인턴쉽 필수 인원보다 작으면 필수인원을 채우기 위해서 팀에서 가져와야함
# 최대 팀을 만들기 위해서는 필수인원을 같은 팀에서 최대한 빼야함.
# 즉 인턴쉽 필수 인원을 얻기 위해서 죽여야할 팀의 개수 파악
# 1 ~ 3명 빼갈때 마다 1팀씩 죽는다.
# 4 ~ 6명 빼갈 때 2팀 죽는다..
n, m, k = map(int, input().split())

teams = min(n // 2, m // 1)

n -= teams * 2
m -= teams * 1

if n + m >= k:
    print(teams)
else:
    k -= (n + m) # 있는 것 먼저 털기
    if k % 3 == 0:
        die = k // 3
    else:
        die = k // 3 + 1
    print(teams - die)
