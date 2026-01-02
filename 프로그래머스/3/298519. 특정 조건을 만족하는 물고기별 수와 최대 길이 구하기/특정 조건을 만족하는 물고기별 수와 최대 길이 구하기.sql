# -- 코드를 작성해주세요
# -- 평균길이 33cm 이상 > 물고기 종류별로 구분 > 잡은수, 최대길이, 물고기의 종류를 출력
# -- 물고기의 종류에 대해서 오름차순
# -- 10cm이하 물고기들은 10cm로 취급

# -- 1. null이거나 10cm이하의 길이들은 10으로 변경해줘야한다.
# -- if문을 썻지만 ifnull이 더 합리적이다.
# -- 왜냐하면 10cm이하의 경우네는 null이기 때문에 10cm이하는 기록되지 않음.
# with tmp as (
#     select ID, FISH_TYPE, if(LENGTH <= 10 or LENGTH is null, 10, LENGTH) as LENGTH
#     from FISH_INFO
# )

# -- group by 쓰고 집계함수 조건 판단할 때는 having절 사용한다.
# select count(ID) as FISH_COUNT, max(LENGTH) as MAX_LENGTH, FISH_TYPE
# from tmp
# group by FISH_TYPE
# having avg(LENGTH) >= 33
# order by FISH_TYPE;







# 평균길이 33cm 이상 물고기 종류별로 분류 잡은 수, 최대길이, 물고기 종류 출력
# 종류 오름차순 / 10cm이하는 10cm로 
# with tmp as (
#     select count(ID) as FISH_COUNT, max(LENGTH) as max_length, FISH_TYPE
#     from FISH_INFO
#     group by FISH_TYPE
#     having avg(if(LENGTH <= 10 or LENGTH is null, 10, LENGTH)) >= 33
# )

# select *
# from tmp
# order by FISH_TYPE asc;

# 평균길이 33cm 이상인 물고기들을 종류별로 분류
# 잡은 수 최대길이 물고기의 종류 출력
# 물고기 종류에 대해 오름차순
# 10cm이하는 10cm로 취급하여 평균
with tmp as (
    select FISH_TYPE
    from FISH_INFO
    group by FISH_TYPE
    having avg(ifnull(LENGTH, 10)) >= 33
)

select count(ID) as 'FISH_COUNT', max(LENGTH) as 'MAX_LENGTH', T.FISH_TYPE
from tmp as T, FISH_INFO as I
where T.FISH_TYPE = I.FISH_TYPE
group by T.FISH_TYPE
order by T.FISH_TYPE;
