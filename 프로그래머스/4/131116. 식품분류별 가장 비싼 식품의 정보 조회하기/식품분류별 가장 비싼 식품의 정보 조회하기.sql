-- 코드를 입력하세요
# 식품별 가격 제일 비싼거
# 식품별 비싼거 - group by + 집계함수
# 식품분류 -  '과자', '국', '김치', '식용유' - where
# 식품 가격 기준 내림차순

with temp as (
    select CATEGORY, max(PRICE) as PRICE
    from FOOD_PRODUCT
    group by CATEGORY
    )
    

select P.CATEGORY, P.PRICE, P.PRODUCT_NAME
from FOOD_PRODUCT P
inner join temp T on (P.CATEGORY = T.CATEGORY and P.PRICE = T.PRICE)
where P.CATEGORY in ('과자', '국', '김치', '식용유')
order by P.PRICE desc;



