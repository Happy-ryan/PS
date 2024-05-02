-- 코드를 작성해주세요
with tmp as (
    select C.ID, C.GENOTYPE as C_TYPE, P.GENOTYPE as P_TYPE
    from ECOLI_DATA as C
    left join ECOLI_DATA as P on C.PARENT_ID = P.ID
)

-- A가 B에 포함되는가 판단 > 비트연산(&) 활용하기
select ID, C_TYPE as GENOTYPE, P_TYPE as PARENT_GENOTYPE
from tmp
where C_TYPE & P_TYPE = P_TYPE
order by ID asc;