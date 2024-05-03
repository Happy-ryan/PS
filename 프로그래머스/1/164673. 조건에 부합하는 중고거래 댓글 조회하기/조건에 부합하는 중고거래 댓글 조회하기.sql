-- 코드를 입력하세요
-- R.WRITER_ID, R.CONTENTS 어디에서 테이블에서 가져오는지 정확하게 따져야함
-- 여기선 R테이블의 WRITER_ID과 CONTENTS를 가져오므로 이 부분을 주의해야한다.
SELECT B.TITLE, B.BOARD_ID, R.REPLY_ID, R.WRITER_ID, R.CONTENTS,
    DATE_FORMAT(B.CREATED_DATE, '%Y-%m-%d') as CREATED_DATE
FROM USED_GOODS_BOARD AS B
INNER JOIN USED_GOODS_REPLY AS R ON B.BOARD_ID = R.BOARD_ID
# WHERE B.CREATED_DATE LIKE '2022-10%'
# WHERE DATE_FORMAT(B.CREATED_DATE, "%Y-%m") = '2022-10'
WHERE YEAR(R.CREATED_DATE) = 2022 and MONTH(R.CREATED_DATE) = 10
ORDER BY R.CREATED_DATE ASC, B.TITLE ASC;


# 2022년 10월 작성된 게시글 제목, 게시글id, 댓글id, 댓글작성자, 댓글내용, 댓글작성일
# 댓글작성일 기준 오름차순 / 게시글 제목 오름차순
select B.TITLE, B.BOARD_ID, R.REPLY_ID, R.WRITER_ID, R.CONTENTS,
        date_format(R.CREATED_DATE, '%Y-%m-%d') as CREATED_DATE
from USED_GOODS_BOARD B
inner join USED_GOODS_REPLY R on B.BOARD_ID = R.BOARD_ID
where year(B.CREATED_DATE) = 2022 and month(B.CREATED_DATE) = 10
order by R.CREATED_DATE asc, B.TITLE asc;


-- 2022년 10월 작성된 게시글 제목, ID, 댓글ID, 댓글작성사ID, 댓글내용, 댓글 작성일
-- 댓글 작성일 기준 오름차순 / 제목 기준 오름차순

select B.TITLE, B.BOARD_ID, R.REPLY_ID, R.WRITER_ID, R.CONTENTS,
        date_format(R.CREATED_DATE, '%Y-%m-%d')
from USED_GOODS_BOARD as B
inner join USED_GOODS_REPLY as R on B.BOARD_ID = R.BOARD_ID
where year(B.CREATED_DATE) = 2022 and month(B.CREATED_DATE) = 10
order by R.CREATED_DATE asc, B.TITLE asc






