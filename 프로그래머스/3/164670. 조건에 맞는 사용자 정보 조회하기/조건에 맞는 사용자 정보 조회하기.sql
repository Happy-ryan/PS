# -- 코드를 입력하세요
# # 게시글 3건 이상 등록한 사용자의 id, 닉네임, 전체주소, 전화번호
# # 전체주소: 시/명/상세주소
# # 전화번호 xxx-xxxx-xxx
# # 회원id기준 내림차순
# with temp as (
#     select WRITER_ID, count(*) AS count
#     from USED_GOODS_BOARD
#     group by WRITER_ID
#     having count >= 3
# )

# select U.USER_ID,
#        U.NICKNAME,
#        concat(U.CITY,
#               ' ',
#               U.STREET_ADDRESS1,
#               ' ',
#               U.STREET_ADDRESS2) as 전체주소,
#        concat(substring(U.TLNO, 1, 3),
#               '-',
#               substring(U.TLNO, 4, 4),
#               '-',
#               substring(U.TLNO, 8)) as 전화번호
# from temp T
# inner join USED_GOODS_USER U on T.WRITER_ID = U.USER_ID
# order by U.USER_ID desc;




# # 중고거래게시물 3건 이상 등록한 사용자의 사용자id, 닉네임, 전체주소, 전화번호 조회
# # 전체주소: 시 / 도로명 / 상세주소
# # 전화번호 xxx-xxxx-xxxxx
# # 회원id기준 내림차순

# with temp as(
#     select WRITER_ID, count(*) as COUNT
#     from USED_GOODS_BOARD
#     group by WRITER_ID
#     having count(*) >= 3
# )

# select  T.WRITER_ID, U.NICKNAME,
#         concat(U.CITY, ' ', U.STREET_ADDRESS1, ' ', U.STREET_ADDRESS2) as 전체주소,
#         concat(substring(TLNO, 1, 3),
#                '-',
#                 substring(TLNO, 4, 4),
#                '-',
#               substring(TLNO, 8)) as 전화번호
# from temp T
# inner join USED_GOODS_USER U on T.WRITER_ID = U.USER_ID
# order by T.WRITER_ID desc;



# # 중고거래 3건이상 / id 닉네임 주소 전화번호
# # 주소 - 시 + 도로명 주소 + 상세주소
# # 전화번호

# with member as (
#     select WRITER_ID, count(*) as COUNT
#     from USED_GOODS_BOARD
#     group by WRITER_ID
#     having COUNT >= 3
# )

# select M.WRITER_ID, U.NICKNAME, 
#     concat(U.CITY, ' ', U.STREET_ADDRESS1, ' ', U.STREET_ADDRESS2) as 전체주소,
#     concat(substring(U.TLNO, 1, 3)
#             ,'-',
#           substring(U.TLNO, 4, 4)
#             ,'-',
#           substring(U.TLNO, 8)) as 전화번호
# from member M
# inner join USED_GOODS_USER U on M.WRITER_ID = U.USER_ID
# order by M.WRITER_ID desc;


# # 중고거래 3건 이상 등록한 사용자
# # 전체주소 - 시, 도로명 주소, 상세주소
# # 전화번호 - 하이픈 형식
# # 회원ID 내림차순 정렬

# with tmp as (
#     select WRITER_ID, count(*) as CNT
#     from USED_GOODS_BOARD
#     group by WRITER_ID
#     having CNT >= 3
# )

# select U.USER_ID,
#        U.NICKNAME,
#        concat(U.CITY, ' ', U.STREET_ADDRESS1, ' ', U.STREET_ADDRESS2) as 전체주소,
#        concat(
#            # substring(필드명, 시작위치(1base), 길이)
#            substring(U.TLNO, 1, 3),
#            '-',
#            substring(U.TLNO, 4, 4),
#            '-',
#            substring(U.TLNO, 8, 4)
#        ) as 전화번호
# from tmp as T
# inner join USED_GOODS_USER as U on T.WRITER_ID = U.USER_ID
# order by  U.USER_ID desc;


# 게시물 3건 이상 등록
with tmp as (
    select WRITER_ID, count(*) as CNT
    from USED_GOODS_BOARD
    group by WRITER_ID
    having CNT >= 3
)

select U.USER_ID,
       U.NICKNAME,
       concat(U.CITY, ' ', U.STREET_ADDRESS1, ' ', U.STREET_ADDRESS2) as 전체주소,
       concat(
            substring(U.TLNO, 1, 3),
            '-',
            substring(U.TLNO, 4, 4),
            '-',
            substring(U.TLNO, 8, 4)
        ) as 전화번호
from tmp as T
inner join USED_GOODS_USER as U on U.USER_ID = T.WRITER_ID
order by  U.USER_ID desc;
