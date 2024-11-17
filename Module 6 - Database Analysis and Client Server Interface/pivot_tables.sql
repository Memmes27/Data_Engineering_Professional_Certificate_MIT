#Intro to pivot_tables
SELECT
	MONTH(payment_date) as month,
    SUM(amount)
FROM payment
WHERE
	YEAR(payment_date) = 2005
GROUP BY 1
;

#functions to handle date and time
SELECT	@@global.time_zone, @@session.time_zone;