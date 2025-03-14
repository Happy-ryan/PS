# 7월의 아이스크림 총 주문량과 상반기의 아이스크림 총 주문량의 합
# 상위 3개 '맛' 조회
# !주의점!
# > FIRST_HALF 에서 flavor는 기본키이므로 맛의 중복이 없다.
# > 하지만 JULY에서는 예시에서 보는 것처럼 맛의 중복이 발생하고 있다. 따라서 이걸 처리해야한다. - temp
with temp as (
    select FLAVOR, sum(TOTAL_ORDER) as TOTAL_ORDER
    from JULY
    group by FLAVOR
),

temp2 as (
    select H.FLAVOR, H.TOTAL_ORDER + T.TOTAL_ORDER as TOTAL_ORDER
    from FIRST_HALF H
    inner join temp T on H.FLAVOR = T.FLAVOR
    order by TOTAL_ORDER desc
)

select FLAVOR
from temp2
limit 3;

with temp3 as (
    select FLAVOR, sum(TOTAL_ORDER) as TOTAL_ORDER
    from FIRST_HALF
    group by FLAVOR

    union all

    select FLAVOR, sum(TOTAL_ORDER) as TOTAL_ORDER
    from JULY
    group by FLAVOR
),
temp4 as (
    select FLAVOR, sum(TOTAL_ORDER) as TOTAL_ORDER
    from temp3
    group by FLAVOR
    order by TOTAL_ORDER desc
)

select FLAVOR
from temp4
limit 3;

with temp5 as (
    select J.FLAVOR, sum(ifnull(H.TOTAL_ORDER, 0) + J.TOTAL_ORDER) as TOTAL_ORDER
    from FIRST_HALF H
    right outer join JULY J on H.SHIPMENT_ID = J.SHIPMENT_ID
    group by J.FLAVOR
    order by TOTAL_ORDER desc
)

select FLAVOR
from temp5
limit 3;

# 7월 아이스크림 총 주문량과 상반기 아이스크림 총 주문량을 더한 값이 큰 순서대로 3개의 맛
with temp as (
    select FLAVOR, sum(TOTAL_ORDER) as TOTAL_ORDER
    from JULY
    group by FLAVOR
), temp2 as (
    select H.FLAVOR, H.TOTAL_ORDER + T.TOTAL_ORDER as TOTAL_ORDER
    from FIRST_HALF H
    inner join temp T on H.FLAVOR = T.FLAVOR
)

select FLAVOR
from temp2
order by TOTAL_ORDER desc
limit 3;

with temp as (
    select FLAVOR, sum(TOTAL_ORDER) as TOTAL_ORDER
    from FIRST_HALF
    group by FLAVOR

    union all

    select FLAVOR, sum(TOTAL_ORDER) as TOTAL_ORDER
    from JULY
    group by FLAVOR
)

select *
from temp;

# 7월의 아이스크림 총 주문량과 상반기의 아이스크름 총 주문량을 더한 값이 큰 순서대로 상위 3개의 맛 조회
# 테이블을 합쳐야함 > 테이블 자체를 다룰 때 union all / union / intersect
with tmp as (
    select FLAVOR, sum(TOTAL_ORDER) as TOTAL_ORDER
    from FIRST_HALF
    group by FLAVOR
    
    union all
    
    select FLAVOR, sum(TOTAL_ORDER) as TOTAL_ORDER
    from JULY
    group by FLAVOR
), tmp2 as (
    select FLAVOR, sum(TOTAL_ORDER) as TOTAL_ORDER
    from tmp
    group by FLAVOR
    order by TOTAL_ORDER desc
)

select FLAVOR
from tmp2
limit 3;

