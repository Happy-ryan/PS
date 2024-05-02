-- 코드를 작성해주세요
-- 2022년 / 평가점수 가장 높은 사원 정보 
-- 상 + 하반기 점수의 합

with total_year as (
    select  EMP_NO, 
            sum(SCORE) as TOTAL_SCORE,
            -- 동점자 같은 순위 부여 rank
            rank() over (order by sum(SCORE) desc) as RN
    from HR_GRADE
    group by EMP_NO
)

select T.TOTAL_SCORE as SCORE, E.EMP_NO, E.EMP_NAME, E.POSITION, E.EMAIL
from total_year as T, HR_EMPLOYEES as E
where T.RN = 1 and T.EMP_NO = E.EMP_NO;