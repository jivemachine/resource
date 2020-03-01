


--case statments
--option 1 CASE, col, WHEN 
select col1,
    case source_column_name,
        WHEN conditional_statement
        THEN value_to_assign
        ELSE other_value_to_assign
    END AS new_column_name
FROM table1
;


select dept_name,
    case dept_name,
        WHEN 'Research' THEN 'Development'
        WHEN 'Marketing' THEN 'Sales'
        ELSE dept_name
    END AS dept_group
FROM departments;



-- option 2: CASE, WHEN, col

select case
        WHEN dept_name IN ('research', 'development') THEN 'R&D'
        WHEN dept_name IN ('sales', 'marketing') THEN "sales&marketing"
        WHEN dept_name IN ('production', 'quality management') THEN "prod&QM"
        else dept_group
    end as dept_group
from departments;

--you cant put aggregate functions withing a case statement but you can
--wrap aggregate functions around a case statement

-- use ELSE  to capture errors or a group idk sabout


## IF STATEMENTS

--IF(source_column_name) [=,>,<,...] = conditional_statement, value_to_assign, other_value_to_assign)


--if you want to return a true or false (1,0) boolean value, do this:

SELECT dept_name, dept_name = 'research'
from departments;

--returns the same as
--if you want it to return one of 2 values based on a single condition, use IF()

SELECT dept_name, IF(dept_name = 'research', true, false)
from departments;

--if you need multiple 'if elif elif ....' please use CASE statements

SELECT CASE
        WHEN birth_date < '1983' THEN "old"
        when gender = "f" then 1
        else 0
    end as gen_x_females
from employees;
