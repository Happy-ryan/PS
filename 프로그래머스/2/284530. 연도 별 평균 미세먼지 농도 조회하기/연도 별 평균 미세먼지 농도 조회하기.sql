-- 코드를 작성해주세요
# 연도별 평균 미세먼지 오염도와 평균 초미세먼지 오염도 조회
# 소수 두 번째자리에서 반올림
# 연도 기준 오름차순
# 수원!!
# select  year(YM) as YEAR,
#         round(avg(PM_VAL1), 2) as 'PM10',
#         round(avg(PM_VAL2), 2) as 'PM2.5'
# from AIR_POLLUTION
# where LOCATION2 = '수원'
# group by YEAR
# order by YEAR;




# 연도별 평균 미세먼지 오염도 / 평균 초미세먼지 오염도
# 소수 세째 자리에서 반올림
# 연도 기준으로 오름차순
select year(YM) as YEAR, round(avg(PM_VAL1), 2) as 'PM10', round(avg(PM_VAL2), 2) as 'PM2.5'
from AIR_POLLUTION
where LOCATION2 = '수원'
group by YEAR
order by YEAR asc;