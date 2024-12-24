# Write your MySQL query statement below


(select name as results
from MovieRating m1 join Users u using(user_id) group by user_id
order by count(rating) DESC,name limit 1 )
UNION ALL
(select m.title as results
from Movies m join MovieRating mr on m.movie_id=mr.movie_id 
where MONTH(created_at)='02' and YEAR(created_at)='2020'
group by m.title 
order by avg(rating) DESC,title  limit 1)
