-- 코드를 입력하세요
# 이 문제 포인트 : 재구매
# 회원id, 재구매상품id
# 회원id 오름차순 / 상품id 내림차순

select USER_ID, PRODUCT_ID
from ONLINE_SALE
group by USER_ID
having count(PRODUCT_ID) > 1
order by USER_ID asc, PRODUCT_ID desc;


SELECT USER_ID,	PRODUCT_ID
FROM ONLINE_SALE
GROUP BY USER_ID, PRODUCT_ID
# 재구매 주의! 1초과해야함
HAVING COUNT(PRODUCT_ID) > 1
ORDER BY USER_ID ASC, PRODUCT_ID DESC;


select USER_ID, PRODUCT_ID 
from ONLINE_SALE
-- 동일한 상품을 재구매..특정 PRODUCT_ID 1 초과!
where SALES_AMOUNT > 1
order by USER_ID asc, PRODUCT_ID desc;



# '동일한 회원'이 '동일한 상품' "재구매" / 회원id기준 오름차순 / 상품id기준 내림차순
with temp as (
    select USER_ID, PRODUCT_ID, count(*) as COUNT
    from ONLINE_SALE
    group by USER_ID, PRODUCT_ID
    having COUNT > 1
)

select USER_ID, PRODUCT_ID
from temp
order by USER_ID asc, PRODUCT_ID desc;


# 동일한 회원이 동일한 상품을 재구매!!  > 회원 / 아이디 묶고 > 다른 행의 수로 재구매 판단!
with tmp as (
    select USER_ID, PRODUCT_ID, count(ONLINE_SALE_ID) as count
    from ONLINE_SALE
    group by USER_ID, PRODUCT_ID
    having count > 1
    order by USER_ID asc, PRODUCT_ID desc
)

select USER_ID, PRODUCT_ID
from tmp;

# '재구매'한 데이터 분석 > 재구매한 회원ID . 재구매 상품 ID 
# 회원 ID 기준 오름차순 / 상품ID 기준 내림차순
# 재구매를 어케 판단할 것 인가? > count 활용
select USER_ID, PRODUCT_ID
from ONLINE_SALE
group by USER_ID, PRODUCT_ID
having count(*) > 1
order by USER_ID asc, PRODUCT_ID desc