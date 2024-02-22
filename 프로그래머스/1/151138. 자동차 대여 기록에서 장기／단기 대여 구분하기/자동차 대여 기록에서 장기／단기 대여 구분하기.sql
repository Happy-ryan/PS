-- 코드를 입력하세요
select  HISTORY_ID, CAR_ID,
        date_format(START_DATE, '%Y-%m-%d'),
        date_format(END_DATE, '%Y-%m-%d'),      
        if((timestampdiff(DAY, START_DATE, END_DATE) + 1)>=30, 
           '장기 대여','단기 대여') as RENT_TYPE
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
where month(START_DATE) = 9
order by HISTORY_ID desc;

SELECT
    HISTORY_ID,
    CAR_ID,
    DATE_FORMAT(START_DATE, '%Y-%m-%d') AS START_DATE,
    DATE_FORMAT(END_DATE, '%Y-%m-%d') AS END_DATE,    
    CASE
        WHEN TIMESTAMPDIFF(DAY, START_DATE, END_DATE) + 1 >= 30 THEN '장기 대여'
        ELSE '단기 대여'
    END AS RENT_TYPE

FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY 
WHERE YEAR(START_DATE) = 2022
    AND MONTH(START_DATE) = 9
ORDER BY HISTORY_ID DESC;


# 대여시작일 2022년 9월 속하는 대여기록
# 대여기간 30일 이상 장기대여 / 그렇지 않으면 단기대여
# 대여기록id 기준 내림차순
# 대여기간 +1 주의!

with temp as (
    select HISTORY_ID, CAR_ID,
        date_format(START_DATE, '%Y-%m-%d') as START_DATE,
        date_format(END_DATE, '%Y-%m-%d') as END_DATE,
        if(timestampdiff(day, START_DATE, END_DATE) + 1 >= 30, '장기 대여', '단기 대여') as RENT_TYPE
    from CAR_RENTAL_COMPANY_RENTAL_HISTORY
    where year(START_DATE) = 2022 and month(START_DATE) = 9
    order by HISTORY_ID desc
)

select *
from temp;