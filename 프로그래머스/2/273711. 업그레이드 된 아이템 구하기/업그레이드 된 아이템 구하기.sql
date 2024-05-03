-- 코드를 작성해주세요
# 아이템 희귀도 RARE
-- 다음 업그레이드!!! 내 자식노들 찾는 것!

with rare as (
    select  C.ITEM_ID as ITEM_ID,
            P2.ITEM_NAME as ITEM_NAME,
            P2.RARITY as RARITY
    from ITEM_INFO as P 
    left join ITEM_TREE as C on P.ITEM_ID = C.PARENT_ITEM_ID
    left join ITEM_INFO as P2 on P2.ITEM_ID = C.ITEM_ID
    where (C.ITEM_ID is not null) and (P.RARITY = 'RARE')
)

select *
from rare
order by ITEM_ID desc;