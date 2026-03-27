-- 보호 시작일 -> ANIMAL_INS에서 DATETIME
# 입양일 -> ANIMAL_OUTS에서 DATETIME
# 입양일 < 보호 시작일

# 아이디, 이름 (보호 시작일이 빠른 순으로)

select i.ANIMAL_ID, i.name
from animal_ins i
join animal_outs o
on i.animal_id = o.animal_id
where i.datetime > o.datetime
order by i.datetime asc
