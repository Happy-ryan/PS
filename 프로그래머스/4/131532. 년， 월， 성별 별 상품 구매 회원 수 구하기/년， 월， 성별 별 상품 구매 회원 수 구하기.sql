-- 코드를 입력하세요
# 구매 년 / 월 / 성별 별로 구매한 회원수
# 년 월 성별 오름차순
# 성별정보 없으면 제거

select  year(O.SALES_DATE) as YEAR,
        month(O.SALES_DATE) as MONTH, 
        U.GENDER,
        count(distinct U.USER_ID) as USERS
from USER_INFO U
inner join ONLINE_SALE O on U.USER_ID = O.USER_ID
where U.GENDER is not null
group by YEAR, MONTH, U.GENDER
order by YEAR asc, MONTH asc, U.GENDER asc;