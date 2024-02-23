# -- 코드를 입력하세요
# SELECT O.ANIMAL_ID, O.NAME
# FROM ANIMAL_OUTS AS O
# # NAME이 아니라 ID로 판단해야함
# # 서브쿼리절 활용
# WHERE  O.ANIMAL_ID NOT IN (SELECT ANIMAL_ID FROM ANIMAL_INS)
# GROUP BY O.ANIMAL_ID
# ORDER BY O.ANIMAL_ID;

#-------#
SELECT O.ANIMAL_ID, O.NAME 
FROM ANIMAL_OUTS AS O
# left join 하면 왼쪽(out)에 있는 테이블 다 들어오고 오른쪽 테이블(in)에는 있는데 왼쪽(out)에 없는 것은 null로 들어옴
LEFT JOIN ANIMAL_INS AS I ON O.ANIMAL_ID = I.ANIMAL_ID
# 없음!
WHERE I.ANIMAL_ID IS NULL
ORDER BY O.ANIMAL_ID;



# 입양 간 기록 o / 보호소 들어온 기록 x
# 동물id, 이름순으로 조회!

select O.ANIMAL_ID, O.NAME
from ANIMAL_OUTS O
left join ANIMAL_INS I on O.ANIMAL_ID = I.ANIMAL_ID
where I.ANIMAL_ID is null;
