-- 코드를 작성해주세요
-- 사원별 성과금 보조 
-- 사번기준 오름차순

-- 1. 상하반기 점수 평균 구하기 테이블

with grade as (
    select EMP_NO, 
        case
            when avg(SCORE) >= 96 then 'S'
            when avg(SCORE) >= 90 then 'A'
            when avg(SCORE) >= 80 then 'B'
            else 'C'
        end as GRADE
    from HR_GRADE
    group by EMP_NO
)

select G.EMP_NO, E.EMP_NAME, G.GRADE, 
        case
            when G.GRADE = 'S' then E.SAL * 0.2
            when G.GRADE = 'A' then E.SAL * 0.15
            when G.GRADE = 'B' then E.SAL * 0.1
            else E.SAL * 0
        end as BONUS
from grade as G
left join HR_EMPLOYEES as E on G.EMP_NO = E.EMP_NO
order by G.EMP_NO asc;
