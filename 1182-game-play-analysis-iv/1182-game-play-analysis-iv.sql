# Write your MySQL query statement below
with next_date_table as 
(select *,
lead(event_date) over (partition by player_id order by event_date)  as next from activity ),

diff_table as 
(select 
datediff(next,min(event_date) ) as diff
from next_date_table
group by player_id)

select 
round((sum(case when diff=1 then 1 else 0 end)/count(*)),2) as fraction from diff_table