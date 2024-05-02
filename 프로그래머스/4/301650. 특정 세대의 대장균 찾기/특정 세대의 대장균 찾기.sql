-- 코드를 작성해주세요

with recursive tree as (
    -- non recursive
    select  ID, 
            PARENT_ID,
            2 as GE
    from ECOLI_DATA
    where PARENT_ID is not null
    
    union all
    
    -- recursive
    select C.ID, C.PARENT_ID, T.GE + 1 
    from ECOLI_DATA as C
    inner join tree as T on C.PARENT_ID = T.ID
)

select ID
from tree
group by ID
having(max(GE) = 3);