-- 코드를 입력하세요
# 구매 년 / 월 / 성별 별로 구매한 회원수
# 년 월 성별 오름차순
# 성별정보 없으면 제거
# 유저id 중복제거 distinct
# ONLINE_SALE테이블에 USER_ID = 1 기록  2022-01-01, 2022-01-25 > 2번의 구매 기록이 존재
# 결과테이블 USERS 1로 되어있음. 즉 USER_ID 1을 가진 사람의 구매기록의 수가 아니라 몇 명이 구매했냐로 판단해야함.
select  year(O.SALES_DATE) as YEAR,
        month(O.SALES_DATE) as MONTH, 
        U.GENDER,
        count(distinct U.USER_ID) as USERS
from USER_INFO U
inner join ONLINE_SALE O on U.USER_ID = O.USER_ID
where U.GENDER is not null
group by YEAR, MONTH, U.GENDER
order by YEAR asc, MONTH asc, U.GENDER asc;


# 판매기록, 대여기록 등 history성격을 가진 컬럼들은 id가 중복될 확률이 매우 높다. 그때는 group by / distinct로 반드시 처리!
# 년 / 월 / 성별 별로 상품을 구매한 회원수!!
# 성별 정보가 없는 경우 제외

select year(S.SALES_DATE) as YEAR, month(S.SALES_DATE) as MONTH, I.GENDER, count(distinct S.USER_ID) as COUNT
from USER_INFO I
inner join ONLINE_SALE S on I.USER_ID = S.USER_ID
where I.GENDER	is not null
group by YEAR, MONTH, I.GENDER;
