-- 코드를 입력하세요
# 테이블 2개 > join
# 조회수가 가장 높은 중고거래 게시물
# 조회수가 가장 높다 > 서브쿼리절로 추출 or 윈도우함수
# FILE ID를 기준으로 내림차순 
select CONCAT("/home/grep/src/", BOARD_ID, "/",FILE_ID, FILE_NAME, FILE_EXT) AS FILE_PATH
from USED_GOODS_BOARD 
inner join USED_GOODS_FILE USING(BOARD_ID) 
WHERE VIEWS = (SELECT MAX(VIEWS) 
               FROM USED_GOODS_BOARD )
ORDER BY FILE_ID DESC;

select concat('/home/grep/src/', B.BOARD_ID, '/', F.FILE_ID, F.FILE_NAME, F.FILE_EXT) as FILE_PATH
from USED_GOODS_BOARD B
inner join USED_GOODS_FILE F on B.BOARD_ID = F.BOARD_ID
where B.VIEWS = (select max(VIEWS) from USED_GOODS_BOARD )
order by F.FILE_ID desc;
