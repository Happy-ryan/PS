-- 코드를 입력하세요
# 7월의 아이스크림 총 주문량과 상반기의 아이스크림 총 주문량의 합
# 상위 3개 '맛' 조회
# FIRST_HALF 에서 flavor는 기본키이므로 맛의 중복이 없다.
# 하지만 JULY에서는 예시에서 보는 것처럼 맛의 중복이 발생하고 있다. 따라서 이걸 처리해야한다.
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