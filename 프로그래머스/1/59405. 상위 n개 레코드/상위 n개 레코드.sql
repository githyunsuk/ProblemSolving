-- 코드를 입력하세요
select name
from (select name 
      from animal_ins
      order by datetime)
where rownum = 1