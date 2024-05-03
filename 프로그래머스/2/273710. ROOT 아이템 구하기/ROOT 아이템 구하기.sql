-- 코드를 작성해주세요
select I.ITEM_ID, I.ITEM_NAME
from ITEM_INFO as I
join ITEM_TREE as T on I.ITEM_ID = T.ITEM_ID
where T.PARENT_ITEM_ID is null
order by I.ITEM_ID asc;
