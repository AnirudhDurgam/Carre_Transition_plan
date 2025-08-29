
Select
    P.firstname, 
    P.lastname, 
    A.city,
    A.state
from Person P left join Address A 
on A.personId=P.personId;
