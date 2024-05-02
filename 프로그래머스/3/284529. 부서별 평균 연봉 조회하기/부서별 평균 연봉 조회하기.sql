-- 코드를 작성해주세요
-- 부서별(Group by) 평균(avg) 연봉
-- 부서ID, 영문 부서명, 평균 연봉
-- round(평균연봉, 0) as AVG_SAL
-- 평균 연봉 기준으로 내림차순

with tmp as (
    select E.DEPT_ID, D.DEPT_NAME_EN, E.SAL
    from HR_EMPLOYEES as E
    left join HR_DEPARTMENT as D on E.DEPT_ID = D.DEPT_ID
)

select DEPT_ID, DEPT_NAME_EN, round(avg(SAL),0) as AVG_SAL
from tmp
group by DEPT_ID, DEPT_NAME_EN
order by avg(SAL) desc; 
