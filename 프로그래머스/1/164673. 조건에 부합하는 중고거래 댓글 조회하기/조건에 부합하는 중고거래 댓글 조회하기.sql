-- 코드를 입력하세요
-- R.WRITER_ID, R.CONTENTS 어디에서 테이블에서 가져오는지 정확하게 따져야함
-- 여기선 R테이블의 WRITER_ID과 CONTENTS를 가져오므로 이 부분을 주의해야한다.
SELECT B.TITLE, B.BOARD_ID, R.REPLY_ID, R.WRITER_ID, R.CONTENTS, DATE_FORMAT(R.CREATED_DATE, '%Y-%m-%d')
FROM USED_GOODS_BOARD AS B
INNER JOIN USED_GOODS_REPLY AS R ON B.BOARD_ID = R.BOARD_ID
-- WHERE B.CREATED_DATE LIKE '2022-10%'
WHERE DATE_FORMAT(B.CREATED_DATE, "%Y-%m") = '2022-10'
ORDER BY R.CREATED_DATE ASC, B.TITLE ASC;


# select A.TITLE, A.BOARD_ID, B.REPLY_ID, B.WRITER_ID, B.CONTENTS,
#         date_format(B.CREATED_DATE, "%Y-%m-%d") as CREATED_DATE
# from USED_GOODS_BOARD A
# inner join USED_GOODS_REPLY B on A.BOARD_ID = B.BOARD_ID
# where year(B.CREATED_DATE) = "2022" and month(B.CREATED_DATE) = "10"
# order by A.CREATED_DATE asc, A.TITLE asc;

