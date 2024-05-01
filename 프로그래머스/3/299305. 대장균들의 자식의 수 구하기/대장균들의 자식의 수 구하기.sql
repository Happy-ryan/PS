-- 코드를 작성해주세요
with tmp as (
    select P.ID, count(C.PARENT_ID) as CHILD_COUNT
    from ECOLI_DATA as P
    left join ECOLI_DATA as C on P.ID = C.PARENT_ID
    group by P.ID
)

select *
from tmp
order by tmp.ID asc;