-- 코드를 입력하세요
# 게시글 3건 이상 등록한 사용자의 id, 닉네임, 전체주소, 전화번호
# 전체주소: 시/명/상세주소
# 전화번호 xxx-xxxx-xxx
# 회원id기준 내림차순
with temp as (
    select WRITER_ID, count(*) AS count
    from USED_GOODS_BOARD
    group by WRITER_ID
    having count >= 3
)

select U.USER_ID,
       U.NICKNAME,
       concat(U.CITY,
              ' ',
              U.STREET_ADDRESS1,
              ' ',
              U.STREET_ADDRESS2) as 전체주소,
       concat(substring(U.TLNO, 1, 3),
              '-',
              substring(U.TLNO, 4, 4),
              '-',
              substring(U.TLNO, 8)) as 전화번호
from temp T
inner join USED_GOODS_USER U on T.WRITER_ID = U.USER_ID
order by U.USER_ID desc;




# 중고거래게시물 3건 이상 등록한 사용자의 사용자id, 닉네임, 전체주소, 전화번호 조회
# 전체주소: 시 / 도로명 / 상세주소
# 전화번호 xxx-xxxx-xxxxx
# 회원id기준 내림차순

with temp as(
    select WRITER_ID, count(*) as COUNT
    from USED_GOODS_BOARD
    group by WRITER_ID
    having count(*) >= 3
)

select  T.WRITER_ID, U.NICKNAME,
        concat(U.CITY, ' ', U.STREET_ADDRESS1, ' ', U.STREET_ADDRESS2) as 전체주소,
        concat(substring(TLNO, 1, 3),
               '-',
                substring(TLNO, 4, 4),
               '-',
              substring(TLNO, 8)) as 전화번호
from temp T
inner join USED_GOODS_USER U on T.WRITER_ID = U.USER_ID
order by T.WRITER_ID desc;