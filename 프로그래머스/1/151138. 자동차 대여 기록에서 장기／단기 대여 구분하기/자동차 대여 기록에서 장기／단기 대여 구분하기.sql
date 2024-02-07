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
        WHEN END_DATE - START_DATE +1 >= 30 THEN '장기 대여'
        ELSE '단기 대여'
    END AS RENT_TYPE

FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY 
WHERE YEAR(START_DATE) = 2022
    AND MONTH(START_DATE) = 9
ORDER BY HISTORY_ID DESC;

SELECT  HISTORY_ID, CAR_ID,
        DATE_FORMAT(START_DATE, '%Y-%m-%d'),
        DATE_FORMAT(END_DATE, '%Y-%m-%d'),      
        CASE
            WHEN TIMESTAMPDIFF(DAY, START_DATE, END_DATE) + 1 >= 30 THEN '장기 대여'
            ELSE '단기 대여'
        END AS RENT_TYPE
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE MONTH(START_DATE) = 9
ORDER BY HISTORY_ID DESC;