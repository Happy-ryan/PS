-- 코드를 입력하세요
# 2021년에 가입한 회원
# 상품을 '구매'한 회원수 와 상품을 구매한 회원 비율
# 년, 월, 별 출력
# 비율은 소수점 두번째자리에서 반올림
# 년 기준 오름차순 / 월 기준 오름차순
# distinct을 반드시 의심해봐!
with temp as (
    select  year(S.SALES_DATE) as YEAR,
            month(S.SALES_DATE) as MONTH,
            # 년/월로 그룹바이를 하다보니 id에 중복이 발생한! group by id하지 않앗음..
            # 판매기록 등에서는 id가 중복되어있을 수 있다.
            # 정답 안나오면 distinct부터 항상 의심하기!
            count(distinct I.USER_ID) as PURCHASED_USERS
    from USER_INFO I
    inner join ONLINE_SALE S on I.USER_ID = S.USER_ID
    where year(I.JOINED) = 2021
    group by YEAR, MONTH
), total_users as (
    select count(USER_ID) as TOTAL
    from USER_INFO
    where year(JOINED) = 2021
)

select  T.YEAR, T.MONTH, T.PURCHASED_USERS,
        round(T.PURCHASED_USERS / U.TOTAL, 1) as PURCHASED_RATIO
from temp T, total_users U
order by T.YEAR asc, T.MONTH asc;


# 2021년 가입한 전체 회원 중 상품을 구매한 회원의비율
# 년, 월별로 출력
# 두번째반올림(round(1)) /년도기준 

with total as (
    select count(*) as COUNT
    from USER_INFO
    where year(JOINED) = 2021
), member as (
    # 판매기록, 대여기록--기록 id 중복 반드시 존재!
    select year(S.SALES_DATE) as YEAR,
            month(S.SALES_DATE) as MONTH,
            # group by 년 / 월 ..예시 2022-01 user_id 1이 아이가 2번 구매! > 1명처리으로 처리해여함
            # 구매한 사람의 수를 원하므로 2명이 아니라 1명으로 처리해여함
            count(distinct I.USER_ID) as COUNT
    from USER_INFO I
    inner join ONLINE_SALE S on I.USER_ID = S.USER_ID	
    where year(I.JOINED) = 2021
    group by YEAR, MONTH
    
)

select M.YEAR, M.MONTH, M.COUNT as PUCHASED_USERS, 
        round(M.COUNT / T.COUNT,1) as PUCHASED_RATIO
from member M, total T;