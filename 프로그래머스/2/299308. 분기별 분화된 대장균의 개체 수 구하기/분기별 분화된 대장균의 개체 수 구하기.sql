-- 코드를 작성해주세요
-- 분기별로 분화된 대장균 개체의 총 수
-- 각 분기에는 Q를 붙이고
-- 분기에 대해서 오름차순

select case
            when month(DIFFERENTIATION_DATE) <= 3 then '1Q'
            when month(DIFFERENTIATION_DATE) <= 6 then '2Q'
            when month(DIFFERENTIATION_DATE) <= 9 then '3Q'
            else '4Q'
        end as QUARTER,
        count(ID) as ECOLI_COUNT
from ECOLI_DATA
group by QUARTER
order by QUARTER;
        