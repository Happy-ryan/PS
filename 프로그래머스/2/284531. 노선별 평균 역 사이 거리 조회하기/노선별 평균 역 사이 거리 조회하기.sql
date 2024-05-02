-- 코드를 작성해주세요
-- 노선별로(group by) 총 누계 거리, 평균 역 사이 거리
-- round(TOTAL_DISTANCE, 1), round(AVERAGE_DISTANCE, 2) concat(+"km")
-- TOTAL_DISTANCE 내림차순

select ROUTE, 
    concat(round(sum(D_BETWEEN_DIST), 1), 'km') as TOTAL_DISTANCE,
    concat(round(avg(D_BETWEEN_DIST), 2), 'km') as AVERAGE_DISTANCE
from SUBWAY_DISTANCE
group by ROUTE
order by sum(D_BETWEEN_DIST) desc;
