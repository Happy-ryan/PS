-- 코드를 입력하세요
# 통풍시트, 열선시트, 가죽시트 하나 이상의 옵션 포함
# 종류별로 몇 대
# 종류 기준으로 오름차순
select CAR_TYPE, count(*) as CARS
from CAR_RENTAL_COMPANY_CAR
where OPTIONS like "%통풍시트%" or OPTIONS like "%열선시트%" or OPTIONS like "%가죽시트%"
group by CAR_TYPE
order by CAR_TYPE;

select CAR_TYPE, count(*) AS CARS
from CAR_RENTAL_COMPANY_CAR
where OPTIONS regexp '통풍시트|열선시트|가죽시트'
group by CAR_TYPE
order BY CAR_TYPE;

# 통풍시트 / 열선시트 / 가죽시트 하나 이상의 옵셥 포함
# 자동차 종류별로 몇 대인지 출력
# 자동차 종류 기준 오름차순
