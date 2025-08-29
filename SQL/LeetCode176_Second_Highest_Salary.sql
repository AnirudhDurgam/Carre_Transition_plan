# Write your MySQL query statement below
-- Select 
--     (Select
--       Distinct(salary) 
--     from Employee 
--     order by salary desc 
--     limit 1 offset 1)   
-- as SecondHighestSalary 

Select 
    Max(salary) as SecondHighestSalary 
from Employee
where salary < 
    (Select 
        Max(salary) 
    from Employee)
