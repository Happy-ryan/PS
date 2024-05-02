-- 코드를 작성해주세요
-- 분화된연도 /분화된 연도별 대장균의 크기의 편차 / id
-- 크기의 편차 = 분화된 연도별 가장 큰 대장균의 크기 - 각 대장균의크기
-- 연도오름차순
-- 대장균의 크기 편차 오름차순
with tmp as (
select year(DIFFERENTIATION_DATE) as DATE, max(SIZE_OF_COLONY) as MAX_SIZE
from ECOLI_DATA
group by year(DIFFERENTIATION_DATE)
)

select  year(D.DIFFERENTIATION_DATE) as YEAR, 
        (T.MAX_SIZE - D.SIZE_OF_COLONY) as YEAR_DEV,
        D.ID
from ECOLI_DATA as D
left join  tmp as T on year(D.DIFFERENTIATION_DATE) = T.DATE
order by year(D.DIFFERENTIATION_DATE) asc, (T.MAX_SIZE - D.SIZE_OF_COLONY) asc;