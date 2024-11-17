-- 1. Basic data verification
SELECT COUNT(*) as total_rows
FROM mrts_data;

-- 2. Check distinct adjustments types
SELECT DISTINCT Adjustments
FROM mrts_data;

-- 3. View sample of data for each adjustment type
SELECT *
FROM mrts_data
WHERE Adjustments = 'Not Adjusted'
LIMIT 5;

-- 4. Check for any NULL values
SELECT 
    COUNT(*) as total_rows,
    SUM(CASE WHEN NAICS_Code IS NULL THEN 1 ELSE 0 END) as null_naics,
    SUM(CASE WHEN Kind_of_Business IS NULL THEN 1 ELSE 0 END) as null_business
FROM mrts_data;

-- 5. Get total sales by month
SELECT 
    SUM(Jan_2017) as Jan_Total,
    SUM(Feb_2017) as Feb_Total,
    SUM(Mar_2017) as Mar_Total
FROM mrts_data
WHERE Adjustments = 'Not Adjusted';

-- 6. View top businesses by total yearly sales
SELECT 
    NAICS_Code,
    Kind_of_Business,
    TOTAL
FROM mrts_data
WHERE TOTAL IS NOT NULL
ORDER BY TOTAL DESC
LIMIT 10;