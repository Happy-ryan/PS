-- 코드를 입력하세요
# ROUNR(평균, 첫번쩨 자리에서 반올림 -> 0)
# 왜냐하면 첫 번째 자리에서 반올림이라고 하면 소숫점이 없는 것. ROUND의 숫자는 몇 번째 자리까지 나타내냐이므로
# 소수 첫째자리에서 반올림하므로 0이 맞다.
SELECT ROUND(AVG(DAILY_FEE),0) AS AVERAGE_FEE
FROM CAR_RENTAL_COMPANY_CAR
WHERE CAR_TYPE = "SUV";

# 평균 > avg
# 소수점 > round(값, 소수어디까지 나타낼거냐?)
# round(15.212, 0) > 소수를 나타내고 싶지 않다 > 소수 첫 번쩨 자리에서 반올림!! 15
# round(15.212, 1) = 15.2
select avg(DAILY_FEE) as AVERAGE_FEE
from CAR_RENTAL_COMPANY_CAR
where CAR_TYPE = 'SUV';

# SUV / 평균일일대여요금 / 소수 첫 번째 자리에서 반올림
select round(avg(DAILY_FEE), 0) as AVERAGE_FEE
from CAR_RENTAL_COMPANY_CAR
where CAR_TYPE = 'SUV'
group by CAR_TYPE;