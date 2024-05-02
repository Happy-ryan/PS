-- 코드를 작성해주세요
-- 분기별로 분화된 대장균 개체의 총 수
-- 각 분기에는 Q를 붙이고
-- 분기에 대해서 오름차순

-- GROUP BY, HAVING, ORDER BY에서 SELECT의 alias를 사용할 수 있다
-- WHEREd에서 SELECT의 alias 사용 불가

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