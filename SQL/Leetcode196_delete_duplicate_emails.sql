
Delete p1
 from person p1  
 join 
 person p2 
 ON p1.Email = p2.Emails
AND p1.Id > p2.Id;

______________________


WITH Ranked AS (
    SELECT 
        Id, 
        Email,
        ROW_NUMBER() OVER (PARTITION BY Email ORDER BY Id) AS rn
    FROM Person
)
DELETE FROM Person
WHERE Id IN (
    SELECT Id FROM Ranked WHERE rn > 1
);
