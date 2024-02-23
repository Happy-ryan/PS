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
            count(distinct I.USER_ID) as PURCHASED_USERS
    from USER_INFO I
    inner join ONLINE_SALE S on I.USER_ID = S.USER_ID
    where year(I.JOINED) = 2021
    group by YEAR, MONTH
), total_users as (
    select count(*) as TOTAL
    from USER_INFO
    where year(JOINED) = 2021
)

select T.YEAR, T.MONTH, T.PURCHASED_USERS, round(T.PURCHASED_USERS / U.TOTAL, 1) as PURCHASED_RATIO
from temp T, total_users U
order by t.YEAR asc, t.MONTH asc;