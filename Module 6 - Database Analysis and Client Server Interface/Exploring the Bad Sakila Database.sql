USE bad_sakila;
SHOW TABLE STATUS;

SELECT COUNT(*), t3.name
FROM film t1 
JOIN film_category t2
	on t1.film_id  = t2.film_id
JOIN category t3
	on t2.category_id = t3.category_id
GROUP BY t3.name;

SELECT active, COUNT(customer_id) as active_customer
FROM customer
GROUP BY 1;

WITH tables AS (
SELECT title , COUNT(t3.length) AS Film_duration
FROM actor t1
JOIN film_actor t2
	ON t1.actor_id = t2.actor_id
JOIN film t3
	ON t2.film_id = t3.film_id
GROUP BY 1
ORDER BY 2 DESC
)
SELECT
*
FROM tables;

SHOW TABLES;

SELECT COUNT(*)
FROM language;

WITH tables AS (
  SELECT
  t1.first_name, COUNT(*)
  FROM actor t1
  JOIN film_actor t2
    ON t1.actor_id = t2.actor_id
  JOIN film t3
    ON t2.film_id = t3.film_id
GROUP BY 1
ORDER BY 1
)
SELECT 
first_name, COUNT(*)
FROM tables
GROUP BY 1 
ORDER BY 1 ;

#Grouping Data and Creating Histograms
SELECT rentals, count(*) as num_customers,
-- RPAD(string, length, rpad_string)
RPAD('', COUNT(*), '*') AS bar
FROM
(
SELECT customer_id, count(rental_id) as rentals
FROM rental
GROUP BY 1) a
group by 1;

#Determine the amount that has been spent by each customer on rentals
SELECT
p.customer_id, SUM(p.amount) as total_amount
FROM payment p
INNER JOIN rental r
	ON p.rental_id = r.rental_id
group by 1;


with table1 AS (
SELECT t1.actor_id, COUNT(*) as num_of_films
FROM actor t1
INNER JOIN film_actor t2
	ON t1.actor_id = t2.actor_id
INNER JOIN film t3
	ON t2.film_id = t3.film_id
GROUP BY 1)
SELECT
num_of_films as films, COUNT(*) as num_actors,
RPAD('', COUNT(*), '*') as bar
FROM table1
group by 1
order by 1;



