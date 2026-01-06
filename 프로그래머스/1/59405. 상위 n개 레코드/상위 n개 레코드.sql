-- 코드를 입력하세요
# SELECT NAME
# FROM ANIMAL_INS
# ORDER BY DATETIME ASC
# # 정렬 후 가장 먼저 들어온 1마리!
# LIMIT 1;

select NAME
from ANIMAL_INS
order by DATETIME asc
limit 1;


# 윈도우함수
with temp as (
    select NAME,
        row_number() over (order by DATETIME asc) as rn
    from ANIMAL_INS
)

select NAME
from temp
where temp.rn = 1;

# 상위 n개..-> limit / 윈도우함수.

select NAME
from
( select NAME, row_number() over (order by DATETIME asc) as rn
 from ANIMAL_INS
) as T
where T.rn = 1;



# 상위 n개 찾는 방법 -> 윈도우 함수 or limit 
# 1) limit
with tmp1 as
    (
    select NAME
    from ANIMAL_INS
    order by DATETIME asc
    limit 1
    )
    
select *
from tmp1;


with tmp1 as (
    select NAME, row_number() over (order by DATETIME asc) as rn
    from ANIMAL_INS
)

select NAME
from tmp1
where rn = 1;

# limit / window / group_concat
select substring_index(group_concat(NAME order by DATETIME asc, '/'), ',', 1) as 'NAME',
        group_concat(NAME separator '/ ')
from ANIMAL_INS;

with tmp as (
    select name, row_number() over (order by DATETIME asc) as rn
    from ANIMAL_INS
    
)

select name
from tmp
where rn = 1;
