-- 코드를 입력하세요
# 테이블에서 조회수가 가장 높은 중고거래 게시물에 대한 첨부파일 경로 조회
# FILE ID 기준 내림차순 / 기본 경로 존재

# step1. 가장 조회수가 많은 게시글 추출

select *
from USED_GOODS_BOARD;

with tmp4 as (
    select BOARD_ID,
        row_number() over (partition by BOARD_ID order by VIEWS desc)
    from USED_GOODS_BOARD
)

select *
from tmp4;


# 테이블 2개 > join
# 조회수가 가장 높은 중고거래 게시물
# 조회수가 가장 높다 > 서브쿼리절로 추출 or 윈도우함수
# FILE ID를 기준으로 내림차순 

-- where절 서브쿼리: max 사용
select concat('/home/grep/src/', B.BOARD_ID, '/', F.FILE_ID, F.FILE_NAME, F.FILE_EXT) as FILE_PATH
from USED_GOODS_BOARD B
inner join USED_GOODS_FILE F on B.BOARD_ID = F.BOARD_ID
where B.VIEWS = (select max(VIEWS) from USED_GOODS_BOARD )
order by F.FILE_ID desc;

-- from절 서브쿼리: row_number 사용
SELECT CONCAT('/home/grep/src/', F.BOARD_ID, '/', F.FILE_ID, F.FILE_NAME, F.FILE_EXT) AS FILE_PATH
FROM USED_GOODS_FILE F
INNER JOIN (
    SELECT B.BOARD_ID,
           ROW_NUMBER() OVER (ORDER BY B.VIEWS DESC) AS VIEWS_RANK
    FROM USED_GOODS_BOARD B
) AS temp ON temp.BOARD_ID = F.BOARD_ID
WHERE temp.VIEWS_RANK = 1
order by F.FILE_ID desc;

-- where절 서브쿼리: limit 사용
select concat('/home/grep/src/', B.BOARD_ID, '/', F.FILE_ID, F.FILE_NAME, F.FILE_EXT) as FILE_PATH
from USED_GOODS_BOARD B
inner join USED_GOODS_FILE F on B.BOARD_ID = F.BOARD_ID
where B.VIEWS = (select VIEWS
                 from USED_GOODS_BOARD
                 order by VIEWS desc
                 limit 1)
order by F.FILE_ID desc;


# 조회수가 가장 높은 중고거래 게시물에 대한 첨부파일 경로 조회
# 첨부파일 경로는 FILE ID 기준 내림차순
# 기본적 파일경로 /home/grep/src/[board id]/[file id],[file name],[file ext]
# 게시글id 기준 디렉토리 구분
# 파일이름 파일id, 파일이름, 확장자로 구성
# 조회수가 가장 높은 것은 하나만 존제

with temp as (
    select BOARD_ID, VIEWS,
        row_number() over (order by VIEWS desc) as rn
    from USED_GOODS_BOARD
)

select concat('/home/grep/src/', T.BOARD_ID, '/', F.FILE_ID, F.FILE_NAME, F.FILE_EXT) as FILE_PATH
from temp T
inner join USED_GOODS_FILE F on T.BOARD_ID = F.BOARD_ID
where T.rn = 1
order by FILE_PATH desc;

# 조회수가 가장 높은 중고거래 게시물(limit, 윈도우함수)
with temp as (
    select BOARD_ID,
        row_number() over (order by VIEWS desc) as rn
    from USED_GOODS_BOARD
)

select concat('/home/grep/src/', F.BOARD_ID, '/',F.FILE_ID, F.FILE_NAME, F.FILE_EXT) as FILE_PATH
from temp T
inner join USED_GOODS_FILE F on T.BOARD_ID = F.BOARD_ID
where T.rn = 1
order by F.FILE_ID desc;


# 조회수가 가장 높은 중고거래 게시물에 대한 첨부파일 경로 조회
# FIELD ID 기준으론 내림차순 정렬
# 기본적 파일경로 =  /home/grep/src/ 
# 게시글ID기준으로 디렉토리 구분
# 파일이름은 파일ID, 이름, 파일확장자로 구성
# 조회수가 가장 높은 게시물은 하나만 존재 <- 최대/ 최소 찾을 때 row_number는 굉장히 유용한 함수

# 1) 최고 조회수 게시물 파악 <- 그룹별로 파악하라는 말을 안했으니까 max만 쓰면 될 듯!
with tmp as (
    select BOARD_ID,
          row_number() over (order by VIEWS desc) as rn
    from USED_GOODS_BOARD 
)

select concat('/home/grep/src/', T.BOARD_ID, '/',  F.FILE_ID, F.FILE_NAME, F.FILE_EXT) as FILE_PATH
from tmp AS T
right join USED_GOODS_FILE AS F on T.BOARD_ID = F.BOARD_ID
where T.rn = 1
order by F.FILE_ID desc;


# 조회수가 가장 높은 중고거래 게시물에 대한 첨부파일 경로 조회
# file id 기준 내림차순
# 조회수가 높은 게시물은 하나만 존재

# 1) 가장 조회수가 높은 게시물 추출
with tmp as (
    select B.BOARD_ID, B.VIEWS,
        F.FILE_ID, F.FILE_EXT, F.FILE_NAME,
    rank() over (order by B.VIEWS desc) as rn
    from USED_GOODS_BOARD as B
    right outer join USED_GOODS_FILE as F on B.BOARD_ID = F.BOARD_ID
)

select concat('/home/grep/src/', BOARD_ID,'/', FILE_ID, FILE_NAME, FILE_EXT) as FILE_PATH
from tmp
where rn = 1
order by FILE_ID desc;