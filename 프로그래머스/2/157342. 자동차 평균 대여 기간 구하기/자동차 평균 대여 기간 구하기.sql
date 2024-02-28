-- 코드를 입력하세요
# 평균대여기간 7일이상
# 대여기간 +1 잊지말자!
# 평균기간 내림차순 id 내림차순
with temp as (
    select CAR_ID, timestampdiff(day, START_DATE, END_DATE) + 1 as DURATION
    from CAR_RENTAL_COMPANY_RENTAL_HISTORY
)

select CAR_ID, round(avg(DURATION), 1) as AVERAGE_DURATION
from temp
group by CAR_ID
having AVERAGE_DURATION >= 7
order by AVERAGE_DURATION desc, CAR_ID desc;





# 평균대여기간 7일 이상
# 소수점 두번째 자리에서 반올림
# 대여기간 내림차순 / id기준 내림차순
# 대여기록, 판매기록...id 중복된다!!
with temp as (
    select CAR_ID, round(avg(timestampdiff(day, START_DATE, END_DATE) + 1), 1) as AVG 
    from CAR_RENTAL_COMPANY_RENTAL_HISTORY
    group by CAR_ID
    having AVG >= 7
)

select *
from temp
order by AVG desc, CAR_ID desc;
