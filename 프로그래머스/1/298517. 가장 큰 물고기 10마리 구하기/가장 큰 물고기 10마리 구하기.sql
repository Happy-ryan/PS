-- 코드를 작성해주세요
# select ID, LENGTH
# from FISH_INFO
# order by LENGTH desc, ID asc
# limit 10;

with tmp as (
    select ID, LENGTH,
            row_number() over(order by LENGTH desc) as rn
    from FISH_INFO
)

select ID, LENGTH
from tmp
where rn between 1 and 10;