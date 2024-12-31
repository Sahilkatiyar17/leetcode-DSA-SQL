# Write your MySQL query statement below
select round((SUM(CASE WHEN order_date=customer_pref_delivery_date THEN 1 else 0 END)/COUNT(*))*100,2) as immediate_percentage
from Delivery where (customer_id,order_date) in 

(select customer_id,min(order_date) 
from Delivery 
group by customer_id
);