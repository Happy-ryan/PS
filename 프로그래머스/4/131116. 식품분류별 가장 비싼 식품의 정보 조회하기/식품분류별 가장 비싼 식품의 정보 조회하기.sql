-- 코드를 입력하세요
# 식품별 가격 제일 비싼거
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

# 각 카테고리별 최대값 가져오기 = substring_index + group_concat
# substring_index(group_concat(P.PRODUCT_NAME order by P.PRICE desc), ',', 1)
select P.CATEGORY, MAX(P.PRICE) as MAX_PRICE, 
       substring_index(group_concat(P.PRODUCT_NAME ORDER BY P.PRICE DESC), ',', 1)
       AS PRODUCT_NAME
from FOOD_PRODUCT P
where P.CATEGORY in ('과자', '국', '김치', '식용유')
group by P.CATEGORY
order by P.PRICE desc;

select CATEGORY, 
       PRICE as MAX_PRICE, 
       PRODUCT_NAME
from FOOD_PRODUCT 
where (CATEGORY, PRICE) in (
    select CATEGORY, max(PRICE)
    from FOOD_PRODUCT 
    where CATEGORY in ('과자', '국', '김치', '식용유')
    group by CATEGORY
)
order by PRICE desc;

# 식품분류별로 가격이 제일 비싼 식품의 정보 얻기
# 식품분류, 과자, 국, 김치, 식용유인경우만 출력!
# 식품 가격 기준 내림차순

with temp as (
    select CATEGORY,PRODUCT_ID,PRODUCT_NAME,PRICE,
        row_number() over(partition by CATEGORY order by PRICE desc) as rn
    from FOOD_PRODUCT
    where CATEGORY regexp '과자|국|김치|식용유'
)

select CATEGORY, PRICE as MAX_PRICE, PRODUCT_NAME
from temp T
where T.rn = 1
order by MAX_PRICE desc;
