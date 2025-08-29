Select 
    C.name as Customers 
from Customers c left join orders o
on c.id=o.customerId 
where o.id is NULL
