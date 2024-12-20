-- 코드를 작성해주세요
# select count(ID) as FISH_COUNT
# from FISH_INFO
# where LENGTH is null;

# length가 10이하인 경우네는 null로 표현이 된다!
# 따라서 10이하의 물고기는 length가 null이다!
select count(*) as FISH_COUNT
from FISH_INFO
where LENGTH is null;