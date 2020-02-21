

SELECT first_name, last_name
FROM employees
WHERE last_name IN ("Vidya", "Maya", "Irena")


subQueries
SELECT column_a, column_b, column_c
FROM table_a
WHERE column_a IN (
    SELECT column_a
    FROM table_b
    WHERE column_b = true
);

SELECT first_name, last_name, birth_date
FROM employees
WHERE emp_no IN (
    SELECT emp_no
    FROM dept_manager
)
LIMIT 10;


--getting the names of employes with a birthday of feb 12th
select title
from titles
where emp_no in (
select emp_no
from salaries
where salary between 67000 and 70000
)

--subqueries selecting employee titles 
--making betwenn 67 and 70k
--and what their job titles are
SELECT title, count(*)
FROM titles
WHERE emp_no IN (
SELECT emp_no
FROM salaries
WHERE salary BETWEEN 67000 AND 70000
AND to_date > now()
)
AND to_date > now()
GROUP BY title

select last_name 





