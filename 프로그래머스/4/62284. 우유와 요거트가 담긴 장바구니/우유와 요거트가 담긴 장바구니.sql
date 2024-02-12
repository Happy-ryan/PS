-- 코드를 입력하세요
# 우유와 요거트 동시 구입한 장바구니
# 장바구니의 id 조회
# id 순으로 오름차순
with milk as (
    select CART_ID
    from CART_PRODUCTS
    where NAME in ('Milk')
), yogurt as (
    select CART_ID
    from CART_PRODUCTS
    where NAME in ('Yogurt')
)

select distinct(M.CART_ID)
from milk M
inner join yogurt Y on M.CART_ID = Y.CART_ID
order by M.CART_ID asc;

with temp as (
    select CART_ID
    from CART_PRODUCTS
    where NAME in ('Milk')
    
    intersect
    
    select CART_ID
    from CART_PRODUCTS
    where NAME in ('Yogurt')
    
)

select CART_ID
from temp
order by CART_ID;