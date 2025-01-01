# Write your MySQL query statement below
select customer_id
from Customer group by customer_id
having count(distinct product_key)=(select count(*) from Product)
#here I did a mistake of writing a number ex-
#count(product_key)=2
#I wrote count is equal to 2 because here product table has only 2 values but it might be different for different test cases.