USE numbers;

SELECT * 
FROM numbers_with_groups;

SELECT
min(n),
max(n),
AVG(n),
count(n)
FROM numbers_with_groups;

SELECT * FROM numbers_with_groups;

SELECT 
category,
count(n),
min(n)
FROM numbers_with_groups
GROUP BY category;

SELECT 
supergroup,
count(n),
max(n)
FROM numbers_with_more_groups
GROUP BY supergroup;

SELECT
	n,
	count(n),
	AVG(n)
FROM numbers_with_more_groups
GROUP BY n;

SELECT 
	category,
	supergroup,
	count(*)
FROM numbers_with_more_groups
GROUP BY category, supergroup;

USE employees;

# How many people were born in each month
SELECT 
	MONTH(birth_date),
	count(*)
FROM employees
GROUP BY MONTH(birth_date);

SELECT 
	MONTH(birth_date),
	count(*),
	max(hire_date),
	min(emp_no)
FROM employees
GROUP BY MONTH(birth_date);

