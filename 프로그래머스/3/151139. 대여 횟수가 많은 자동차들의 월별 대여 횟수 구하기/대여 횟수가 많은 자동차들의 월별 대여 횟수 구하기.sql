-- 코드를 입력하세요
# 대여시작일 기준 22년 8월 ~ 10월
# 총 대여 횟수 5회 이상 자동차들에 대해서
# 월별 자동차 id별 총 대여 횟수
# 월을 기준 오름차순, id 기준 내림차순
# 특정 월의 대여회수 0인 경우 제외 -> 이것때문에 문제가 발생했을듯
select month(START_DATE) as MONTH, CAR_ID, count(*) as RECORDS
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
where month(START_DATE) between 8 and 10 and
    CAR_ID in ( select CAR_ID
                from CAR_RENTAL_COMPANY_RENTAL_HISTORY
                where month(START_DATE) between 8 and 10
                group by CAR_ID
                having count(*) >= 5)
group by month(START_DATE), CAR_ID
order by month(START_DATE) asc, CAR_ID desc ;

select month(START_DATE) as MONTH, CAR_ID, count(*) as RECORDS
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
where START_DATE between '2022-08-01' and '2022-10-31' and
        CAR_ID in (select CAR_ID 
                  from CAR_RENTAL_COMPANY_RENTAL_HISTORY
                  where START_DATE between '2022-08-01' and '2022-10-31'
                  group by CAR_ID
                  having count(*) >= 5)
group by month(START_DATE), CAR_ID
order by month(START_DATE) asc, CAR_ID desc;

SELECT MONTH(START_DATE) AS MONTH, CAR_ID, COUNT(*) AS RECORDS
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY h
WHERE START_DATE BETWEEN '2022-08-01' AND '2022-10-31'
AND EXISTS (
    SELECT 1
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
    WHERE CAR_ID = h.CAR_ID
    AND START_DATE BETWEEN '2022-08-01' AND '2022-10-31'
    GROUP BY CAR_ID
    HAVING COUNT(*) >= 5
)
GROUP BY MONTH(START_DATE), CAR_ID
ORDER BY MONTH(START_DATE) ASC, CAR_ID DESC;



# 대여시작일 기준 2022년 8월 ~ 10월까지 대여횟수가 5회 이상
# 월별 자동차 id별 총 대여 횟수
# 월을 기준 오름차순 / id기준 내림차순 / 대여횟수가 0인 경우 제외
# 개수 셀 때는 count이다!
# 특정기간 동안 총 대여 횟수가 5회인 자동차id 추출 
with temp as (
    select CAR_ID, count(*) as RECORDS
    from CAR_RENTAL_COMPANY_RENTAL_HISTORY
    where year(START_DATE) = 2022 and month(START_DATE) between 8 and 10
    group by CAR_ID
    having count(*) >= 5
)

select month(H.START_DATE) as MONTH, T.CAR_ID, count(*) as RECORDS
from temp T
left join CAR_RENTAL_COMPANY_RENTAL_HISTORY H on T.CAR_ID = H.CAR_ID
# where month(H.START_DATE) between 8 and 10
group by T.CAR_ID, month(H.START_DATE)
order by MONTH asc, T.CAR_ID desc;


# 대여 시작일 기준 202208 ~ 202210까지 총 대여 횟수 5회 이상 
# 월별, 자동차id별 대여횟수 출력 -> 월과 자동차에 대해 모두 group by가 쓰임을 알 수 있다.

# 1) 5회 이상인 car_id 찾기
with tmp as (
    select car_id, count(*) as records
    from CAR_RENTAL_COMPANY_RENTAL_HISTORY
    where start_date between '2022-08-01' and '2022-10-31'
    group by car_id
    having records >= 5
)

# 2) car_id를 통해서 month 추출

select month(H.START_DATE) as MONTH, T.car_id as CAR_ID,  count(*) as RECORDS
from tmp as T
inner join CAR_RENTAL_COMPANY_RENTAL_HISTORY as H on T.car_id = H.car_id
where H.start_date between '2022-08-01' and '2022-10-31'
group by CAR_ID, MONTH
order by MONTH asc, CAR_ID desc;

# MONTH	CAR_ID	RECORDS
# 8	28	3
# 8	27	5
# 8	25	5
# 8	23	3
# 8	19	1
# 8	15	2
# 8	13	5
# 8	11	1
# 8	10	3
# 8	8	6
# 8	7	4
# 8	5	4
# 8	2	5
# 9	28	2
# 9	27	1
# 9	25	6
# 9	23	4
# 9	21	1
# 9	20	4
# 9	19	3
# 9	18	4
# 9	15	2
# 9	13	4
# 9	12	4
# 9	11	6
# 9	10	5
# 9	8	5
# 9	7	1
# 9	5	1
# 9	2	1
# 10	23	1
# 10	21	5
# 10	20	2
# 10	19	1
# 10	18	3
# 10	15	2
# 10	13	5
# 10	12	2
# 10	10	3
# 10	8	5
# 10	7	1
# 10	2	1

# 총 대여 횟수가 5회 이상인 아이의 번호
with tmp as (
    select CAR_ID
    from CAR_RENTAL_COMPANY_RENTAL_HISTORY
    where year(START_DATE) = 2022 and MONTH(START_DATE) between 8 and 10
    group by CAR_ID
    having count(CAR_ID) >= 5
)

select month(START_DATE) as 'month', car_id, count(*) as 'RECORDS'
from CAR_RENTAL_COMPANY_RENTAL_HISTORY as H
where CAR_ID in (
    select CAR_ID
    from CAR_RENTAL_COMPANY_RENTAL_HISTORY
    where year(START_DATE) = 2022 and MONTH(START_DATE) between 8 and 10
    group by CAR_ID
    having count(CAR_ID) >= 5
) and START_DATE between '2022-08-01'and '2022-10-31'
group by car_id, month
order by MONTH asc, CAR_ID desc;