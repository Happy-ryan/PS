-- 코드를 입력하세요
# 평균대여기간 7일이상
# 대여기간 +1 잊지말자!
with temp as (
    select CAR_ID, timestampdiff(day, START_DATE, END_DATE) + 1 as DURATION
    from CAR_RENTAL_COMPANY_RENTAL_HISTORY
)

select CAR_ID, round(avg(DURATION), 1) as AVERAGE_DURATION
from temp
group by CAR_ID
having AVERAGE_DURATION >= 7
order by AVERAGE_DURATION desc, CAR_ID asc;

SELECT car_id , ROUND ( AVG ( timestampdiff(day, START_DATE, END_DATE) + 1) , 1) AS AVERAGE_DURATION
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY 
GROUP BY car_id
HAVING AVERAGE_DURATION >= 7
ORDER BY AVERAGE_DURATION DESC, car_id DESC;