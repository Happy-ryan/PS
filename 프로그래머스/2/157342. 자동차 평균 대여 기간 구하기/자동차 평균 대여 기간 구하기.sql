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










# 평균 대여 기간이 7일 이상인 자동차들의 자동차ID / 평균대여기간
# 평균 대여 기간은 소수점 두번째 자리에서 반올림
# 평균 대여기 기간 기준 내림차순 / 자동차ID 기준 내림차순

# 대여기간은 항상 timestampdiff(기준, 시작, 마감) + 1

# CAR_ID 기준 평균대여기간을 계산한 테이블 tmp
with tmp as (
    select CAR_ID, round(avg(timestampdiff(day, START_DATE, END_DATE) + 1), 1) AS avg_date
    from CAR_RENTAL_COMPANY_RENTAL_HISTORY
    group by CAR_ID  
    having avg_date >= 7 # where는 group by 전 / having은 group by된 집계함수에 대해서 체크
)

select CAR_ID, avg_date
from tmp
order by avg_date desc, CAR_ID desc;





# 평균 대겨 기간 7일 이상 자동차의 자동차id와 평균대여기간
# 평균 대여 기간 소수점 두 번째 자리에서 반올림
# 평균 대여 기간 기준 내림차순 / id 내림차순
# 대여기간 +1 항상 하기!!

with tmp as (
    select car_id, round(avg(timestampdiff(day, START_DATE, END_DATE) + 1), 1) as avg_date
    from CAR_RENTAL_COMPANY_RENTAL_HISTORY
    group by car_id
    having avg_date >= 7
)

select *
from tmp
order by avg_date desc, car_id desc;