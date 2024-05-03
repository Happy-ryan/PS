-- 코드를 작성해주세요
-- 자식이 없다 = 업그레이드할 수 없다.
select P.ITEM_ID, P.ITEM_NAME, P.RARITY 
from ITEM_INFO as P
left join ITEM_TREE as C on P.ITEM_ID = C.PARENT_ITEM_ID
where C.ITEM_ID is null
order by  P.ITEM_ID desc;