-- 코드를 작성해주세요
# select ID, LENGTH
# from FISH_INFO
# order by LENGTH desc, ID asc
# limit 10;

# row_number() over(partition by 필드 order by 필드) as rn
# with tmp as (
#     select ID, LENGTH,
#             row_number() over(order by LENGTH desc) as rn
#     from FISH_INFO
# )

# select ID, LENGTH
# from tmp
# where rn between 1 and 10
# order by LENGTH desc, ID asc;


# select T.ID, T.LENGTH
# from(
#     select ID, LENGTH, row_number() over(order by LENGTH desc) as rn
#     from FISH_INFO
# ) as T
# where rn between 1 and 10
# order by T.LENGTH desc, T.ID asc;

# group concat
# select substring_index(group_concat(ID order by LENGTH desc, ID asc), ',', 1, 10) 
# from FISH_INFO;

select T.ID, T.LENGTH
from (
    select  ID,
            LENGTH,
            row_number() over(order by LENGTH desc) as rn
    from FISH_INFO
) as T
where T.rn between 1 and 10
order by T.LENGTH desc, T.ID asc;

