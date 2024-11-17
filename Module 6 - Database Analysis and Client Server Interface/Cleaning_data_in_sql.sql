#Grouping data in bins

SELECT 
CASE 
	WHEN total <= 75 THEN 'up to 75'
    WHEN total <= 100 THEN '75 to 100'
    WHEN total <= 125 THEN '100 to 125'
    WHEN total <= 150 THEN '125 to 150'
    WHEN total <= 175 THEN '150 to 175'
    WHEN total <= 200 THEN '175 to 200'
ELSE '200+' END AS bin,
COUNT(*) as count
FROM (
SELECT customer_id, SUM(amount) as total
FROM payment
GROUP BY 1
ORDER BY total desc) a
GROUP BY 1;

#Deleting duplicates
SELECT records, count(*)
FROM
(
	SELECT customer_id, first_name, last_name, count(*) as records
    FROM customer
    GROUP BY 1,2,3
    ORDER BY records DESC
) a
GROUP BY 1;

#Cleaning Data pt1
SELECT *,
CASE
	WHEN gender = 'Female' THEN 'female'
    WHEN gender = 'f' THEN 'female'
    WHEN gender = 'FEM' THEN 'female'
    ELSE gender END AS gender_cleansed
FROM customer;

#Data cleaning pt2
SELECT title, rating, original_language_id,
COALESCE(original_language_id, 'unknown') as OriginalLanguage
FROM film;

SELECT *
FROM film;

SELECT *,
	replace(rental_rate,'0', '1') AS clean
From film;

SELECT COUNT(*),
FLOOR(YEAR(birthdate)/10) * 10 AS decade
FROM customer
GROUP BY 2;

