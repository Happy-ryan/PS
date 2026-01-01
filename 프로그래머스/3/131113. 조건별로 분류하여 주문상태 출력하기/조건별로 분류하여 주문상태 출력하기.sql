-- 코드를 입력하세요
# 5월1일 기준 주문id, 제품id, 출고일자, 출고여부
# 출고여부: 5/1일 까지 출고완료
# 이후 날 짜는 출고대기
# 미정이면 출고미정 > case when then end as
# 주문id 오름차순 > order by asc

select ORDER_ID, PRODUCT_ID, date_format(OUT_DATE,'%Y-%m-%d') as OUT_DATE,
        case
            when OUT_DATE is null then '출고미정'
            when timestampdiff(day, '2022-05-01', OUT_DATE) > 0 then '출고대기'
            else '출고완료'
        end as 출고여부
from FOOD_ORDER
order by ORDER_ID asc;


# 5월 1일까지 출고완료 이후 날짜는 출고 대기 / 미지정이면 출고미정
# 예시를 잘 보자! 출고 완료, 미정, 대기 3가지 이므로 case when then end문을 사용해여함
# 주문id기준 오름차순

select ORDER_ID, PRODUCT_ID, date_format(OUT_DATE, '%Y-%m-%d') as OUT_DATE,
        case
            when OUT_DATE is null then '출고미정'
            when timestampdiff(day, '2022-05-01', OUT_DATE) > 0 then '출고대기'
            else '출고완료'
        end as 출고여부
from FOOD_ORDER
order by ORDER_ID asc;


# 2022년 5월 1일
# 출고여부(OUT_DATE) 2022년 5월 1일까지 출고완료
# 이 후 날짜 출고 대기
# 미정이면 출고미정
# 주문ID기준 오름차순 정렬

select ORDER_ID, PRODUCT_ID, date_format(OUT_DATE, '%Y-%m-%d') as OUT_DATE,
        case
            when timestampdiff(day, '2022-05-01', OUT_DATE) > 0 then '출고대기'
            when OUT_DATE is null then '출고미정'
            else '출고완료'
        end as 출고여부
from FOOD_ORDER
order by ORDER_ID asc;


select ORDER_ID, PRODUCT_ID, date_format(OUT_DATE, '%Y-%m-%d') as OUT_DATE,
    case
        when timestampdiff(day, '2022-05-01',OUT_DATE) + 1 >= 2 then '출고대기'
        when OUT_DATE is null then '출고미정'
        else '출고완료'
    end as '출고여부'
from FOOD_ORDER
order by ORDER_ID asc;
