-- 코드를 입력하세요
# 생산일자 2022년 5월 식품들의 식품id, 이름, 총매출
# 총매출 내림차순, 식품id 오름차순

# order table에서 id 당 mount를 집계해야함!
with temp as (
    select PRODUCT_ID, sum(AMOUNT) as AMOUNT
    from FOOD_ORDER 
    where year(PRODUCE_DATE) = 2022 and month(PRODUCE_DATE) = 5 	
    group by PRODUCT_ID
)

select T.PRODUCT_ID, P.PRODUCT_NAME	, T.AMOUNT * P.PRICE as TOTAL_SALES
from temp T
inner join FOOD_PRODUCT P on T.PRODUCT_ID = P.PRODUCT_ID
order by TOTAL_SALES desc, T.PRODUCT_ID asc;
