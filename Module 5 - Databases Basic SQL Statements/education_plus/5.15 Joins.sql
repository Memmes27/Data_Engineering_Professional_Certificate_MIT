SELECT
*
FROM books b
JOIN collegebooks cb
	ON b.BookID = cb.BookID
JOIN colleges c
	ON c.CollegeID = cb.CollegeID;