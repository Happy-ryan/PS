-- 코드를 입력하세요
# 중복되지 않은 8자리 상품코드 > 앞 2자리는 카테고리 코드!
# 카테고리 코드 기준 오름차순
select substring(PRODUCT_CODE, 1, 2) as CATEGORY, count(*) as PRODUCTS
from PRODUCT
group by CATEGORY;

select substring(PRODUCT_CODE, 1, 2) as CATEGORY, count(*) as PRODUCTS
from PRODUCT
group by CATEGORY
order by CATEGORY asc;












# 카테고리 코드별 상품의 개수 
# 카테고리 코드 기준 오름차순

with tmp as (
    select substring(PRODUCT_CODE, 1, 2) as CATEGORY, count(*) as PRODUCTS
    from PRODUCT
    group by CATEGORY
    order by CATEGORY asc
)

select *
from tmp;