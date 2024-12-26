-- 코드를 입력하세요
# 2022년 10월 5일 등록
# 게시글ID,작성사ID,게시글 제목, 가격, 거래상태 조회
# SALE이면 판매중 / RESERVED이면 예약중 / DONE이면 거래완료
# 게시글ID 내림차순
# select BOARD_ID, WRITER_ID, TITLE, PRICE,
#         case
#             when STATUS = 'SALE' then '판매중'
#             when STATUS = 'RESERVED' then '예약중'
#             else '거래완료'
#         end as STATUS
# from USED_GOODS_BOARD
# where year(CREATED_DATE) = 2022 and month(CREATED_DATE) = 10 and day(CREATED_DATE) = 5
# order by BOARD_ID desc;


# 2022년 10월 5일 등록된 중고거래 게시물 ID / 작성자ID / 게시글 제목 / 가격 / 거래상태 조회
# 거래상태 SALE - 판매중 / RESERVED - 에약중 / DONE - 거래완료
# 게시글 ID 기준 내림차순 정렬

select BOARD_ID, WRITER_ID, TITLE, PRICE,
        case 
            when STATUS = 'SALE' then '판매중'
            when STATUS = 'RESERVED' then '예약중'
            when STATUS = 'DONE' then '거래완료'
        end as STATUS
from USED_GOODS_BOARD
where year(CREATED_DATE) = 2022 and month(CREATED_DATE) = 10 and day(CREATED_DATE) = 5
order by BOARD_ID desc;
