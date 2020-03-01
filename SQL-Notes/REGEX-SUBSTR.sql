SELECT 
concat("employee #", emp_no, " is ", first_name, " ", last_name)
FROM employees
LIMIT 10;

SELECT 
	concat(first_name, last_name)
	FROM employees
	LIMIT 10;
	
# LITERAL VALUE - is a value that appears in ther source code that is literally the thing itself

SELECT 
concat (first_name, ' ', last_name) AS full_name
FROM employees
LIMIT 10;

SELECT
first_name,
first_name REGEXP "^[a-f].*"
FROM employees
LIMIT 10;

SELECT 
first_name,
substr(first_name, 1, 1)
FROM employees
LIMIT 10;

SELECT 
first_name,
substr(first_name,1,1)
FROM employees
WHERE substr(first_name,1,1) IN ("a","b","c","d","e","f")
LIMIT 10;

SELECT *
FROM departments;

SELECT *,
REPLACE (dept_no, "d00", "dept_no.")
FROM departments;

# We're in UTC on the server 

SELECT 
now(),
curdate(),
curtime();


#How many days old is each employee
SELECT
	birth_date,
	datediff(now(), birth_date) / 365.25 AS years_old
FROM employees
LIMIT 50;

# average employee age
SELECT
	AVG(datediff(now(), birth_date) / 365.25) AS "Average Employee age"
FROM employees;





