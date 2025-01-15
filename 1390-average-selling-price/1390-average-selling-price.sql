select p.product_id , IFNULL(round(sum(p.price*s.units)/sum(s.units),2),0) as average_price
from Prices p left join UnitsSold s on 
p.product_id=s.product_id
and s.purchase_date<= p.end_date 
and s.purchase_date>=p.start_date
group by p.product_id;


