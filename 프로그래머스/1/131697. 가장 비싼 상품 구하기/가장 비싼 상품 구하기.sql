-- 코드를 입력하세요
SELECT MAX(PRICE) AS MAX_PRICE
FROM PRODUCT;

SELECT PRICE AS MAX_PRICE 
FROM PRODUCT 
ORDER BY PRICE DESC 
LIMIT 1;

# 윈도우 함수, 집계함수, Limit\
with temp as (
    select PRICE, row_number() over(order by PRICE desc) as rn
    from PRODUCT
)

select PRICE as MAX_PRICE
from temp
where temp.rn = 1;

# 판매 중인 상품 / 가장 높은 판매가
with tmp as (
select PRICE,
       row_number() over(order by PRICE desc) as rn
from PRODUCT
)

select PRICE as MAX_PRICE
from tmp
where rn = 1;

