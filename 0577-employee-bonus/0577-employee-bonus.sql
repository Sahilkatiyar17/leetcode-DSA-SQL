
# Write your MySQL query statement below
select e1.name,b.bonus 
from Bonus b right join Employee e1 on b.empId=e1.empId where b.bonus<1000 or b.bonus is NULL;
