-- 코드를 입력하세요
# 2022년 3월 / 온.오프라인 판매날짜, 상품id, 유저id, 판매량
# 오파라인 판매데이터의 경우 userid = null
# 판매일 기준 오름차순 / 상푸id 오름차순 / 유저id 오름차순
# 온라인과 오프라인 테이블을 합치는 것이 포인트...
with tmp_union as (
    select date_format(SALES_DATE, '%Y-%m-%d') as SALES_DATE,
            PRODUCT_ID,
            USER_ID,
            sum(SALES_AMOUNT) as SALES_AMOUNT
    from ONLINE_SALE
    where year(SALES_DATE) = 2022 and month(SALES_DATE) = 3
    group by PRODUCT_ID
    
    union all
    
    select date_format(SALES_DATE, '%Y-%m-%d') as SALES_DATE,
            PRODUCT_ID,
            null as USER_ID,
            sum(SALES_AMOUNT) as SALES_AMOUNT
    from OFFLINE_SALE
    where year(SALES_DATE) = 2022 and month(SALES_DATE) = 3
    group by PRODUCT_ID
)

select *
from tmp_union
order by SALES_DATE asc, PRODUCT_ID asc, USER_ID asc;


# 2022년 3월
# 오프라인 / 온라인 상품의 판대 데이터
# 판매 날짜, 상품id, 유저id, 판매량
# 오프라인 user_id 는 null로 표시 > 오프라인 테이블에는 user_id 컬럼 없음 NULL 도입
# 판매일 오름차순, 상품id 오름차순, 유저id 오름차순
# join은 사용불가할 것 같다...왜냐하면 오프라인 또는 온라인 판매 데이터 중 사라지는 존재가 발생함.
with temp as (
    select date_format(SALES_DATE,'%Y-%m-%d') as SALES_DATE,
        PRODUCT_ID,
        USER_ID,
        SALES_AMOUNT
    from ONLINE_SALE
    where year(SALES_DATE) = 2022 and month(SALES_DATE) = 3
    
    union all
    
    select date_format(SALES_DATE,'%Y-%m-%d') as SALES_DATE,
            PRODUCT_ID,
            NULL as USER_ID,
            SALES_AMOUNT
    from OFFLINE_SALE
    where year(SALES_DATE) = 2022 and month(SALES_DATE) = 3    
    
)

select *
from temp
order by SALES_DATE, PRODUCT_ID, USER_ID;

# 2022년 3월 오프라인/온라인 상품의 판매데이터 판매날짜, 상품id, 유저id, 판매량
# 오프라인 유저id는 null로 표시
# 판매일 기준 오름차순 > 상품id 오름차순 > 유저id 오름차수


with temp as (
    select date_format(SALES_DATE, '%Y-%m-%d') as SALES_DATE,
            PRODUCT_ID, USER_ID, SALES_AMOUNT
    from ONLINE_SALE
    where year(SALES_DATE) = 2022 and month(SALES_DATE) = 3
    
    union all
    
    select date_format(SALES_DATE, '%Y-%m-%d') as SALES_DATE,
            PRODUCT_ID, null as USER_ID, SALES_AMOUNT
    from OFFLINE_SALE
    where year(SALES_DATE) = 2022 and month(SALES_DATE) = 3
)

select *
from temp
order by SALES_DATE asc, PRODUCT_ID	 asc, USER_ID asc;

# 2022년 3월 오프라인/온라인 상품 판매 데이터의 판매날짜, 상품ID, 유저ID, 판매량
# user_id 는 null
# 판매일 asc, 상품ID asc, 유저ID asc

# 온 + 오프라인 테이블 합침 > intersect / union / union all
select date_format(SALES_DATE, '%Y-%m-%d') as SALES_DATE, PRODUCT_ID, USER_ID, SALES_AMOUNT
from ONLINE_SALE
where year(SALES_DATE) = 2022 and month(SALES_DATE) = 3

union all

select date_format(SALES_DATE, '%Y-%m-%d') as SALES_DATE, PRODUCT_ID, null, SALES_AMOUNT
from OFFLINE_SALE
where year(SALES_DATE) = 2022 and month(SALES_DATE) = 3

order by SALES_DATE asc, PRODUCT_ID	 asc, USER_ID asc;