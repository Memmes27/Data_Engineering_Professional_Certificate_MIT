#Write a Query to Return FirstName, LastName, BirthDate, Age - Formula TIMESTAMPDIFF()
SELECT
CONCAT(FirstName, ' ', LastName) as FullName,
BirthDate,
timestampdiff(YEAR, BirthDate, Current_Date()) as Age
FROM students;

#Write a query to Return College Name, Student Population * 100, and a projected 20% growth
SELECT Name,
Students * 1000 AS Student_Population,
(Students * 1000) * 1.2 AS Student_Growth
FROM Colleges;

#Write a query using comparison operator to find students born after 1990
SELECT
*
FROM students
WHERE BirthDate >= '1990-01-01'
ORDER BY BirthDate ASC;

#Write a query to select all the students that are born after 1950 from Tx and Austin
SELECT
*
FROM students
WHERE NOT(BirthDate < '1950-01-01') AND Region = 'TX' AND City = 'Austin';

#Write a query to select all students from Austin, Boston and Chicago
SELECT
*
FROM students
WHERE City IN ('Austin','Boston', 'Chicago');

#Write a query to find students born between 1990 and 2000
SELECT *
FROM students
WHERE BirthDate BETWEEN '1990-01-01' AND '2000-01-01'
ORDER BY BirthDate;

#Write a query to find students with a phone from the "students" table
SELECT
*
FROM students
WHERE Phone IS NOT NULL;

#Write a query to find students with an area code of (541) or gmail address
SELECT
*
FROM students
WHERE Email LIKE ('%gmail.com') OR Phone LIKE ('(541)%');